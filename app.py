from flask import Flask
app = Flask(__name__)

@app.route("/")
#def hello():
#    return "Hello, Ilahlou"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

symbol = 'TQQQ'
import yfinance as yf
df=yf.download(tickers=symbol, period="50d", interval="1D")


def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
    return ema
ema = calculate_ema(df['Close'], 20)


#Plot
price_X = np.arange(df.shape[0]) # Creates array [0, 1, 2, 3, ..., df.shape[0]]
ema_X = np.arange(20, df.shape[0]+1) # Creates array [10, 11, 12, 13, ..., df.shape[0]+1]
                                     # We start at 10, because we use the first 10 values to calculate the SMA,
                                     # then we calculate EMA form the 11th value

plt.xlabel('Days')
plt.ylabel('Price')
plt.plot(price_X, df['Close'], label='Closing Prices')
plt.plot(ema_X, ema, label='EMA')
plt.legend()
plt.show()
