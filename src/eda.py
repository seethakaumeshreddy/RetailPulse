import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading cleaned dataset...")

df = pd.read_csv("data/cleaned_retail.csv")

print(df.head())

# -----------------------------
# Top 10 Products
# -----------------------------

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    "reports/top_products.png"
)

plt.show()

# -----------------------------
# Top 10 Countries
# -----------------------------

top_countries = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries by Sales")

plt.tight_layout()

plt.savefig(
    "reports/top_countries.png"
)

plt.show()

# -----------------------------
# Monthly Sales Trend
# -----------------------------

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

df["Month"] = (
    df["InvoiceDate"]
    .dt.to_period("M")
)

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

plt.figure(figsize=(14,6))

monthly_sales.plot()

plt.title("Monthly Sales Trend")

plt.tight_layout()

plt.savefig(
    "reports/monthly_sales.png"
)

plt.show()

print("\nEDA Complete")