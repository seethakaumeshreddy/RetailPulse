# segmentation page
import streamlit as st
import pandas as pd

st.title("Customer Segmentation")

df = pd.read_csv(
    "data/customer_segments.csv"
)

st.dataframe(df.head())

st.write(
    df["Cluster"].value_counts()
)