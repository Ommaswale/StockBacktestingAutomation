import yfinance as yf
import pandas as pd
from datetime import datetime


# CREATE TICKER INSTANCE FOR A STOCK
print()
stock_symbol = input("Enter the stock symbol: ")
print()
stock_ticker = yf.Ticker(stock_symbol)


# Define the arguments for the history function
start_date = '2020-01-01'
end_date = '2023-05-10'
          #end_date = datetime.now().strftime('%Y-%m-%d')
interval = '1D'


# GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
stock_symbol_hist = stock_ticker.history(start=start_date, end=end_date, interval=interval)
          #data = yf.download(tickers = 'reliance.ns', period = 'max', interval = '1D')


# Save the data to a CSV file
filename = stock_symbol + '_' + start_date + '_' + end_date + '_' + interval + '_data.csv'
stock_symbol_hist.to_csv(filename)
print('Data saved to', filename)


