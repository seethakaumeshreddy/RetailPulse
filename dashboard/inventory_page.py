import streamlit as st
import pandas as pd

st.title("Inventory Optimization")

df = pd.read_csv(
    "data/inventory_recommendations.csv"
)

st.dataframe(df.head(50))

st.bar_chart(
    df.head(20).set_index("Product")
    ["RecommendedStock"]
)