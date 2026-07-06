import streamlit as st
import pandas as pd

st.title("Demand Forecasting")

df = pd.read_csv(
    "data/forecast_results.csv"
)

st.subheader("Forecast Data")

st.dataframe(df.head(20))

st.line_chart(df["yhat"])