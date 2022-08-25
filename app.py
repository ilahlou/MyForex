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

#Plot
price_X = np.arange(df.shape[0])

plt.xlabel('Days')
plt.ylabel('Price')
plt.plot(price_X, df['Close'], label='Closing Prices')
plt.legend()
plt.show()
