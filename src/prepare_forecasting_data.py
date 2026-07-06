import pandas as pd

print("Loading cleaned dataset...")

df = pd.read_csv(
    "data/cleaned_retail.csv"
)

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

daily_sales = (
    df.groupby("InvoiceDate")
    ["Sales"]
    .sum()
    .reset_index()
)

daily_sales.columns = [
    "ds",
    "y"
]

daily_sales.to_csv(
    "data/forecast_data.csv",
    index=False
)

print("forecast_data.csv created")
print(daily_sales.head())