from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Ilahlou"
symbol = 'AUDCAD=X'
import yfinance as yf
df=yf.download(tickers=symbol, period="5d", interval="1D")
df
