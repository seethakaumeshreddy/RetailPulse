import streamlit as st

st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="wide"
)

st.title("📊 RetailPulse Dashboard")

from streamlit_option_menu import option_menu

with st.sidebar:

    page = option_menu(
        menu_title="RetailPulse",
        options=[
            "RetailPulse Overview",
            "Sales Dashboard",
            "Customer Dashboard",
            "Forecast Dashboard",
            "Inventory Dashboard"
        ],
        icons=[
            "house",
            "bar-chart",
            "people",
            "graph-up",
            "boxes"
        ],
        default_index=0
    )

if page == "RetailPulse Overview":

    st.write("Retail Analytics Dashboard")

elif page == "Sales Dashboard":

    exec(open("dashboard/forecasting_page.py").read())

elif page == "Customer Dashboard":

    exec(open("dashboard/churn_page.py").read())

elif page == "Forecast Dashboard":

    exec(open("dashboard/forecasting_page.py").read())

elif page == "Inventory Dashboard":

    exec(open("dashboard/inventory_page.py").read())