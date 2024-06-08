import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Initialize buy and sell columns
data['buy'] = 0
data['sell'] = 0

# Initialize successful_trade and failed_trade lists
successful_trade = []
failed_trade = []
total_trade = []

# Loop through the data
for i in range(1, len(data)):
    # Check for buy signal
    if data['10ma'][i] > data['50ma'][i] and data['10ma'][i-1] <= data['50ma'][i-1]:
        data['buy'][i] = 1
        # Check for successful or failed trade
        if data['Close'][i] * 1.05 <= max(data['High'][i:]):
            successful_trade.append(i)
        elif data['Close'][i] * 0.98 >= min(data['Low'][i:]):
            failed_trade.append(i)

    # Check for sell signal
    if data['10ma'][i] < data['50ma'][i] and data['10ma'][i-1] >= data['50ma'][i-1]:
        data['sell'][i] = -1
        # Check for successful or failed trade
        if data['Close'][i] * 0.95 >= min(data['Low'][i:]):
            successful_trade.append(i)
        elif data['Close'][i] * 1.02 <= max(data['High'][i:]):
            failed_trade.append(i)

# Print results
print('Successful trades:', len(successful_trade))
print('Failed trades:', len(failed_trade))
print('Total percentage profit:', (len(successful_trade)*5) - (len(failed_trade)*2), '%')
