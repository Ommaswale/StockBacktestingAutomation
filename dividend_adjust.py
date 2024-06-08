# Import pandas library
import pandas as pd

# Read stock data from CSV file
stock_data = pd.read_csv('C:/Users/shinchan/reliance.ns_2020-01-01_2023-05-10_1D_data.csv')

# Fill missing values in dividend column with 0
stock_data['Dividends'] = stock_data['Dividends'].fillna(0)

# Calculate dividend factor using formula: 1 - (dividend / close)
stock_data['dividend_factor'] = 1 - (stock_data['Dividends'] / stock_data['Close'])

# Group by symbol and calculate cumulative product of dividend factor
stock_data['cumulative_dividend_factor'] = stock_data['dividend_factor'].cumprod()

# Adjust open, high, low, close prices by multiplying them with cumulative dividend factor
adjusted_columns = ['Open', 'High', 'Low', 'Close']
for col in adjusted_columns:
    stock_data[col + '_adjusted'] = stock_data[col] * stock_data['cumulative_dividend_factor']

# Adjust volume by dividing it with cumulative dividend factor
stock_data['volume_adjusted'] = stock_data['Volume'] / stock_data['cumulative_dividend_factor']
stock_data['volume_adjusted'] = stock_data['volume_adjusted'].round(2)

# Round adjusted prices and volumes to two decimal places
for col in adjusted_columns:
    stock_data[col + '_adjusted'] = stock_data[col + '_adjusted'].round(2)

# Drop unnecessary columns
stock_data.drop(['Dividends', 'dividend_factor'], axis=1, inplace=True)

# Save adjusted data to CSV file
stock_data.to_csv('adj_' + 'reliance.ns_2020-01-01_2023-05-10_1D_data.csv')
