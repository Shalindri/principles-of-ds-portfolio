# principles-of-ds-portfolio
Principles of data science portfolio

# Question 01
# 📊 AWPLR Prediction API (Flask + ML) 🚀

This is a Flask-based **machine learning API** that predicts the **Average Weighted Prime Lending Rate (AWPLR)** for the next **six months** based on consumer price inflation indicators. The trained model is stored as a **serialized `.pkl` file**, which is loaded for inference. The API is deployed on **Render** for cloud-based predictions.

---

## 🚀 Features
✅ Predicts **AWPLR** for the next **6 months**  
✅ Uses **NCPI_Headline, NCPI_Core, CCPI_Headline** as input features  
✅ **Flask API** for real-time predictions  
✅ **Deployed on Render** for easy access  
✅ Model trained using **LSTM (Deep Learning)**  

---

## 📂 Folder Structure


awplr_prediction/ # code related to question 1 of the portfolio

  │   ├── templates/        # HTML templates for UI
  │       ├── index.html    # Web UI for user input
  │── model/                # Model storage
  │   ├── lstm_awplr_model.pkl   # Trained ML model (saved using joblib)
  │   ├── scaler.pkl        # saved StandardScaler (for feature scaling)
  │── data/                 # Dataset storage
  │   ├── awplr_inflation_data.csv  #Raw dataset
  │── notebooks/ # all the jupyter notebook files used for ETL, EDA and Model Training
  │── requirements.txt      # Dependencies (Flask, TensorFlow, joblib, etc.)
  │── app.py      # flask application
GM_data_analysis/ # code related to question 2 of the portfolio
  │── data/# Dataset storage
  │ 
  │── report.ipynb/ #jupyter notebook files used for ETL, EDA and Model Training


  
---

## 📌 **1️⃣ AWPLR Prediction API**
This project contains a **Flask-based machine learning API** that predicts the **Average Weighted Prime Lending Rate (AWPLR)** for the next **six months** based on **consumer price inflation indicators**.

### 🚀 **How to Run**
### **1️⃣ Setup Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
