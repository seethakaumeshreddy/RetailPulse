import streamlit as st
import pandas as pd

st.title("Customer Churn Analysis")

df = pd.read_csv(
    "data/churn_predictions.csv"
)

st.dataframe(df.head())

st.bar_chart(
    df["ChurnRisk"].value_counts()
)