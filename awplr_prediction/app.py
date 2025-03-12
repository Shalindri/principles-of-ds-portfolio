from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

app = Flask(__name__)

# Load the trained LSTM model from pkl
model = joblib.load("./model/lstm_awplr_model.pkl")

# Load the StandardScaler used during training
scaler = joblib.load("./model/scaler.pkl")  # Ensure you've saved the scaler

# Define expected feature columns
features = ["AWPLR", "NCPI_Headline", "NCPI_Core", "CCPI_Headline",
            "AWPLR_MA_3", "AWPLR_MA_6", "AWPLR_LAG_1", "AWPLR_DIFF"]

sequence_length = 6  # Model expects 6 timesteps
num_features = len(features)  # 8 features

def compute_derived_features(df):
    """ Computes the AWPLR_MA_3, AWPLR_MA_6, AWPLR_LAG_1, and AWPLR_DIFF automatically """
    df = df.copy()
    df["AWPLR_MA_3"] = df["AWPLR"].rolling(window=3).mean()
    df["AWPLR_MA_6"] = df["AWPLR"].rolling(window=6).mean()
    df["AWPLR_LAG_1"] = df["AWPLR"].shift(1)
    df["AWPLR_DIFF"] = df["AWPLR"].diff()

    # Fill missing values
    df.fillna(method="bfill", inplace=True)
    return df

def inverse_transform(scaler, predictions):
    """ Reverts the scaled predictions back to original values """
    predictions = np.array(predictions).reshape(-1, 1)
    padded_predictions = np.concatenate((predictions, np.zeros((predictions.shape[0], num_features - 1))), axis=1)
    return scaler.inverse_transform(padded_predictions)[:, 0]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if len(data["sequence"]) != 6:
            return jsonify({"error": "Expected 6 timesteps of data"}), 400

        # Convert input JSON to DataFrame
        df = pd.DataFrame(data["sequence"], columns=["AWPLR", "NCPI_Headline", "NCPI_Core", "CCPI_Headline"])

        # Compute missing features
        df = compute_derived_features(df)

        # Scale the data using the same scaler
        scaled_data = scaler.transform(df[features])

        # Reshape for LSTM (1 sample, 6 timesteps, 8 features)
        current_input = np.array(scaled_data).reshape(1, sequence_length, num_features)

        # Rolling Forecast for Next 6 Months
        future_predictions = []
        for _ in range(6):
            next_prediction = model.predict(current_input)
            future_predictions.append(next_prediction[0, 0])
            current_input = np.roll(current_input, -1, axis=1)  # Shift left
            current_input[0, -1] = 0.8 * current_input[0, -2] + 0.2 * next_prediction  # Update last timestep

        # Convert scaled predictions back to original values
        future_predictions_original = inverse_transform(scaler, future_predictions)

        return jsonify({"predicted_awplr": future_predictions_original.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
