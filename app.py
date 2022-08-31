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
#def hello():
#    return "Pair: AUDCAD=X"

def hello():
    st.set_page_config(page_title='Forex Report')
    st.title('Hello Forex Trade Report🎈 📈')
    st.subheader('Feed me with your Excel file')

    uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
    if uploaded_file:
        st.markdown('---')
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        del df['Ref #']
        del df['Commissions & Fees']
        del df['Amount']
        del df['Time']
        del df['Balance']

        df.loc[df['Amount(USD)'].isin(['--'])] = '0'
        df = df[(df['Type'] == 'TRD')]
        df.loc[df.Description.str.contains('AUD/CAD'), 'Pair'] = 'AUD/CAD'
        df.loc[df.Description.str.contains('AUD/CHF'), 'Pair'] = 'AUD/CHF'
        df.loc[df.Description.str.contains('AUD/USD'), 'Pair'] = 'AUD/USD'
        df.loc[df.Description.str.contains('CAD/CHF'), 'Pair'] = 'CAD/CHF'
        df.loc[df.Description.str.contains('EUR/CHF'), 'Pair'] = 'EUR/CHF'
        df.loc[df.Description.str.contains('EUR/GBP'), 'Pair'] = 'EUR/GBP'
        df.loc[df.Description.str.contains('EUR/USD'), 'Pair'] = 'EUR/USD'
        df.loc[df.Description.str.contains('GBP/CAD'), 'Pair'] = 'GBP/CAD'
        df.loc[df.Description.str.contains('GBP/USD'), 'Pair'] = 'GBP/USD'
        df.loc[df.Description.str.contains('NZD/CAD'), 'Pair'] = 'NZD/CAD'
        df.loc[df.Description.str.contains('NZD/USD'), 'Pair'] = 'NZD/USD'
        df.loc[df.Description.str.contains('USD/CAD'), 'Pair'] = 'USD/CAD'
        df.loc[df.Description.str.contains('USD/CHF'), 'Pair'] = 'USD/CHF'
        del df['Description']
        del df['Type']
    
        st.dataframe(df)
 
   
        groupby_column = st.selectbox(
            'What would you like to analyse?',
            ('Date', 'Pair'),
        )

        # -- GROUP DATAFRAME
        output_columns = ['Amount(USD)']
        df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

    
        # -- PLOT DATAFRAME
        fig = px.bar(
            df_grouped,
            x=groupby_column,
            y='Amount(USD)',
            #color='Profit',
            color_continuous_scale=['red', 'yellow', 'green'],
            template='plotly_white',
            title=f'<b>P/L by {groupby_column}</b>'
        )
        st.plotly_chart(fig)

        # -- PLOT DATAFRAME2
        fig2 = px.scatter(df, x="Date", y="Amount(USD)", color="Pair", hover_data=['Pair'],color_continuous_scale='Inferno')
        st.plotly_chart(fig2)
    
        # -- Plot 3

        fig3 = px.scatter_3d(df, x='Date', y='Pair', z='Amount(USD)', color = 'Pair',hover_data=['Amount(USD)'])
        fig3.update_traces(marker=dict(size=4))
        st.plotly_chart(fig3)
