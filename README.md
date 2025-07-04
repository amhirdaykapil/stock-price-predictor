# 📈 Stock Price Predictor

This project is a **Stock Price Predictor** that uses **Linear Regression** to predict future stock prices based on historical data. It also comes with a **Streamlit web app** for interactive predictions.

---

## 📸 Screenshots

### 🖥️ Streamlit Web App
![Web App Homepage](images/app_homepage.png)

### 📊 Graph
![Graph](images/graph.png)

### 🖥️ Prediction Graph
![Prediction Graph](images/prediction_example.png)

---

## 🚀 Features
- 📥 Download historical stock data (Yahoo Finance API)
- 📊 Visualize stock trends
- 🤖 Predict stock prices using Linear Regression
- 🌐 Streamlit app for user-friendly interface

---

## 🛠 Technologies Used
- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-Learn
- TensorFlow & Keras
- Streamlit

---

## 📂 Project Structure
    Stock-Price-Predictor/
    ├── app.py # Streamlit Web App
    ├── data_downloader.py # Download stock data
    ├── stock_predictor.py # CLI based prediction
    ├── requirements.txt # Python dependencies
    ├── LICENSE
    └── README.md

---

## 📦 Installation
    1. Clone the repository:
        git clone https://github.com/<your-username>/stock-price-predictor.git

    2. Install dependencies:
        pip install -r requirements.txt

    3. Run Streamlit app:
        streamlit run app.py