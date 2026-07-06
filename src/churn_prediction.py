import pandas as pd

print("Loading Customer Segments...")

df = pd.read_csv(
    "data/customer_segments.csv"
)

# High recency = customer inactive
df["ChurnRisk"] = df["Recency"].apply(
    lambda x: "High"
    if x > 180
    else "Low"
)

df.to_csv(
    "data/churn_predictions.csv",
    index=False
)

print("churn_predictions.csv created")

print(
    df["ChurnRisk"].value_counts()
)