import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta

# Fetch stock data
ticker = 'GME'
data = yf.download(ticker, start='2024-01-01', end='2024-07-19')

# Calculate moving averages
data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)
data['SMA200'] = ta.trend.sma_indicator(data['Close'], window=200)

# Calculate Relative Strength Index (RSI)
data['RSI'] = ta.momentum.rsi(data['Close'], window=14)

# Calculate MACD
data['MACD'] = ta.trend.macd(data['Close'])
data['MACD_Signal'] = ta.trend.macd_signal(data['Close'])

print(data['RSI'])
print(data['MACD'])
print(data['SMA200'])
print(data['SMA50'])

'''
# Plotting the data
plt.figure(figsize=(14, 7))


# Price and Moving Averages
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA50'], label='50-day SMA')
plt.plot(data['SMA200'], label='200-day SMA')
plt.title(f'{ticker} Price and Moving Averages')
plt.legend()

# RSI
plt.subplot(3, 1, 2)
plt.plot(data['RSI'], label='RSI')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')
plt.title('Relative Strength Index (RSI)')
plt.legend()

# MACD
plt.subplot(3, 1, 3)
plt.plot(data['MACD'], label='MACD')
plt.plot(data['MACD_Signal'], label='MACD Signal')
plt.title('MACD')
plt.legend()

plt.tight_layout()
plt.show()

'''
