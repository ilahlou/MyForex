from flask import Flask
import numpy as np
import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import seaborn as sns
import importlib_metadata

app = Flask(__name__)

@app.route("/")
#def hello():
#    return "Pair: AUDCAD=X"

#def index():
#    return "Congratulations, it's a web app!"

#@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
