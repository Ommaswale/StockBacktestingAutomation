import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the csv file into a pandas dataframe
df = pd.read_csv("reliance.ns_data.csv")

# Set the index column to be the date column
df = df.set_index("Date")

# Convert the index column to datetime format
df.index = pd.to_datetime(df.index)

# Calculate the 10ma and 50ma
df["10ma"] = df["Close"].rolling(10).mean()
df["50ma"] = df["Close"].rolling(50).mean()

# Plot the closing price of the stock
plt.plot(df["Close"])

# Plot the 10ma and 50ma
plt.plot(df["10ma"], label="10ma", color="green")
plt.plot(df["50ma"], label="50ma", color="red")

# Add a title and labels
plt.title("Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")

# Show the plot
plt.show()

# Create two new columns for buy signal and sell signal with default values of 0
df["buy_signal"] = 0
df["sell_signal"] = 0

# Shift the 10ma column by 1 row to get the previous value
df["prev_10ma"] = df["10ma"].shift(1)
# Shift the 50ma column by 1 row to get the previous value
df["prev_50ma"] = df["50ma"].shift(1)

# Assign 1 to buy signal if there is a crossover from below
df["buy_signal"] = np.where((df["10ma"] > df["50ma"]) & (df["prev_10ma"] < df["prev_50ma"]), 1, df["buy_signal"])
# Assign 1 to sell signal if there is a crossover from above
df["sell_signal"] = np.where((df["10ma"] < df["50ma"]) & (df["prev_10ma"] > df["prev_50ma"]), 1, df["sell_signal"])

# Drop the prev_10ma and prev_50ma columns as they are no longer needed
df = df.drop(["prev_10ma", "prev_50ma"], axis=1)

# Show the plot
plt.show()
