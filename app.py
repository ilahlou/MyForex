from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Pair: AUDCAD=X"

import yfinance as yf


symbol = 'AUDCAD=X'

def Data():
    return yf.download(tickers=symbol, period="5d", interval="15m")

print(df)
