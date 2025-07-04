import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.title('Stock Price Predictor App')


ticker = st.text_input('Enter Stock Ticker (e.g., AAPL, MSFT, TSLA):', 'AAPL')


if st.button('Fetch & Predict'):
    st.write(f"Fetching data for: **{ticker}**")
    data = yf.download(ticker, start='2015-01-01', end='2024-12-31')
    data.reset_index(inplace=True)


    st.subheader('Closing Price History')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data['Date'], data['Close'])
    st.pyplot(fig)


    data['Close_next'] = data['Close'].shift(-1)
    data = data[:-1]
    X = np.array(data['Close']).reshape(-1, 1)
    y = np.array(data['Close_next']).reshape(-1, 1)


    lr = LinearRegression()
    lr.fit(X, y)
    y_pred = lr.predict(X)

 
    st.subheader('Actual vs Predicted Closing Prices')
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.scatter(X, y, color='blue', s=10, label='Actual')
    ax2.plot(X, y_pred, color='red', label='Predicted')
    ax2.set_xlabel('Today\'s Closing Price')
    ax2.set_ylabel('Next Day\'s Closing Price')
    ax2.legend()
    st.pyplot(fig2)

  
    accuracy = lr.score(X, y)
    st.success(f"Model Accuracy: {accuracy * 100:.2f}%")
