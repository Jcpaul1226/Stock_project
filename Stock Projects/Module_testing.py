import yfinance as yf
import string
from Level_testing import calculate_support_resistance


ticker = input("What Ticker symbol are you interested in: ")
stock_data = yf.download(ticker, start='2024-07-01', end='2024-07-19')

GME = yf.Ticker(ticker)

#print(GME.info['sharesOutstanding'])
#print(GME.get_shares_full(start="2002-01-01", end=None))
#print(GME.history(period='5d'))
#print(GME.major_holders)
print("Current Price: ", GME.info['currentPrice'])
print("industy: ", GME.info['industry'])
print("Sector: ", GME.info['sector'])
print("Level of Resistance: ")
print("Level of Support: ")
print("Volatility: ")
print("PeGRatio: ", GME.info['pegRatio'])
