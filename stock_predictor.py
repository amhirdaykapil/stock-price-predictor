import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf


data = yf.download('AAPL', start='2015-01-01', end='2024-12-31')
data.reset_index(inplace=True)


print("First 5 rows of the dataset:")
print(data.head())

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price history')
plt.title('AAPL Closing Price History')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend()
plt.show()

data['Close_next'] = data['Close'].shift(-1) 
data = data[:-1] 

X = np.array(data['Close']).reshape(-1, 1) 
y = np.array(data['Close_next']).reshape(-1, 1)  
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


lr_model = LinearRegression()
lr_model.fit(X_train, y_train)


y_pred = lr_model.predict(X_test)


plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  
plt.scatter(X_test, y_pred, color='red', label='Predicted Prices')  
plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Closing Price USD ($)")
plt.ylabel("Next Day Closing Price USD ($)")
plt.legend()
plt.show()


accuracy = lr_model.score(X_test, y_test)
print(f"Model Accuracy (R^2 Score): {accuracy * 100:.2f}%")
