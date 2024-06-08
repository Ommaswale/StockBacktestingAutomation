def candlesticks(df, w=1, format='%d-%m-%y'):
    
    prices = copy(df.dropna())
    prices.reset_index(inplace=True)
    if 'Date' in prices:
        prices['Date'] = prices['Date'].apply(mpl_dates.date2num)
    else:
        prices['Datetime'] = prices['Datetime'].apply(mpl_dates.date2num)
    try:
        del prices['Adj close']
        del prices['Volume']
    except:
        pass
    
    fig, ax = plt.subplots(figsize = [10,7])
    
    candlestick_ohlc(ax, prices.values, width=w, colorup='green', colordown='red', alpha=0.8);
    date_format = mpl_dates.DateFormatter(format)
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    
#candlesticks(df)