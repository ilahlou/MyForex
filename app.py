from flask import Flask
import numpy as np
import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module
import seaborn as sns
import os
import importlib_metadata

app = Flask(__name__)

@app.route("/")
def hello():
    return "Pair: AUDCAD=X"


