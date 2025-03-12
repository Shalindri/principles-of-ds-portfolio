
# PRINCIPLES OF DATA SCIENCE PORTFOLIO
## Question 01
## 📊 AWPLR Prediction 🚀

This project provides a **Flask-based machine learning API** that predicts the **Average Weighted Prime Lending Rate (AWPLR)** for the next **six months** based on consumer price inflation indicators. The trained model is stored as a `.pkl` file, loaded for inference, and served via a REST API.

---

## 🚀 **How to Run the Application Locally**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### **2️⃣ Set Up Virtual Environment**
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run Flask App**
```bash
python app.py
```
📌 **Local URL:** 👉 `http://127.0.0.1:5000/`

---

## ☁️ **Deployed API on Render**
If you don’t want to run it locally, use the live API hosted on **Render**:

📌 **Base URL:** 👉 `https://your-app-name.onrender.com`

---

## 📡 **API Endpoints**
### 🔹 **1️⃣ Predict AWPLR (POST)**
**Endpoint:**  
```http
POST /predict
```

**Request Format (JSON)**:
```json
{
    "sequence": [
        {"AWPLR": 10.25, "NCPI_Headline": 150.3, "NCPI_Core": 145.6, "CCPI_Headline": 135.8},
        {"AWPLR": 10.30, "NCPI_Headline": 151.2, "NCPI_Core": 146.3, "CCPI_Headline": 136.1},
        {"AWPLR": 10.35, "NCPI_Headline": 152.0, "NCPI_Core": 147.1, "CCPI_Headline": 136.5},
        {"AWPLR": 10.40, "NCPI_Headline": 153.1, "NCPI_Core": 148.0, "CCPI_Headline": 137.2},
        {"AWPLR": 10.45, "NCPI_Headline": 154.0, "NCPI_Core": 149.2, "CCPI_Headline": 137.8},
        {"AWPLR": 10.50, "NCPI_Headline": 155.2, "NCPI_Core": 150.5, "CCPI_Headline": 138.5}
    ]
}
```

**Response Format (JSON)**:
```json
{
    "predicted_awplr": [10.55, 10.60, 10.65, 10.70, 10.75, 10.80]
}
```
## 📂 Folder Structure
```
awplr_prediction/
│── app.py                # 🚀 Main Flask application file
│── templates/            # 📂 Web UI (HTML templates)
│   ├── index.html        # 🎨 Web form for input & prediction
│── model/                # 📂 Trained model storage
│   ├── lstm_awplr_model.pkl  # 🤖 Trained LSTM model (joblib)
│   ├── scaler.pkl        # 📏 Scaler for feature normalization
│── data/                 # 📂 Dataset storage
│   ├── awplr_inflation_data.csv  # 📊 Raw dataset
│── notebooks/            # 📂 Jupyter notebooks for ETL, EDA, Model Training
│── requirements.txt      # 📜 Dependencies for AWPLR prediction
│── .gitignore            # 🚫 Ignore unnecessary files
```
## Question 02

## 📊 Analyze General Motor Bankruptcy in 2009

Analyze Genaral Motors company sales and stock data and provide insigts data using EDA


# 📊 AWPLR Prediction API (Flask + ML) 🚀

This project provides a **Flask-based machine learning API** that predicts the **Average Weighted Prime Lending Rate (AWPLR)** for the next **six months** based on consumer price inflation indicators. The trained model is stored as a `.pkl` file, loaded for inference, and served via a REST API.

---

## 📂 Folder Structure
```
GM_data_analysis/
│── data/                 # 📂 Dataset storage
│── report.ipynb          # 📂 Jupyter notebook for ETL, EDA, Model Training
```



