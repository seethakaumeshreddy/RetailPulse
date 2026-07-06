import pandas as pd
from datetime import timedelta

print("Loading cleaned dataset...")

df = pd.read_csv("data/cleaned_retail.csv")

# Convert date column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Snapshot date
snapshot_date = df["InvoiceDate"].max() + timedelta(days=1)

# RFM calculation
rfm = df.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "Invoice": "nunique",
    "Sales": "sum"
})

# Rename columns
rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

print("\nFirst 10 Customers:")
print(rfm.head(10))

print("\nShape:")
print(rfm.shape)

# Save file
rfm.to_csv(
    "data/rfm_data.csv"
)

print("\nrfm_data.csv created successfully")