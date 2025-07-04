import yfinance as yf
import pandas as pd

stock_symbol = "AAPL"

start_date = "2015-01-01"
end_date = "2024-07-01"

data = yf.download(stock_symbol, start=start_date, end=end_date)

data.to_csv(f"{stock_symbol}_stock_data.csv")

print(f"Downloaded data for {stock_symbol} from {start_date} to {end_date}")
print(data.head())
