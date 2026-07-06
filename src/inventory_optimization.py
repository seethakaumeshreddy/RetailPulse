import pandas as pd

df = pd.read_csv(
    "data/cleaned_retail.csv"
)

inventory = (
    df.groupby("Description")
    ["Quantity"]
    .sum()
    .reset_index()
)

inventory.columns = [
    "Product",
    "TotalSold"
]

inventory["RecommendedStock"] = (
    inventory["TotalSold"] * 1.2
)

inventory.to_csv(
    "data/inventory_recommendations.csv",
    index=False
)

print(
    "inventory_recommendations.csv created"
)