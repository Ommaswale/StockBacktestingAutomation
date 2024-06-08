import pandas as pd
import datetime

def get_stock_data(symbol, start_date, end_date, timeframe):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    url = f"https://finance.google.com/finance/historical?q={symbol}&startdate={start.strftime('%b+%d,+%Y')}&enddate={end.strftime('%b+%d,+%Y')}&output=csv"
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    if timeframe == 'weekly':
        data = data.resample('W').last()
    elif timeframe == 'monthly':
        data = data.resample('M').last()
    return data

# Example usage
data = get_stock_data('SBIN', '2022-01-01', '2022-12-31', 'weekly')

data.to_csv('SBIN_weekly.csv')