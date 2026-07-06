import pandas as pd

print("Loading combined dataset...")

df = pd.read_csv("data/combined_retail.csv")

print("Original Shape:")
print(df.shape)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove rows with missing Customer ID
df = df.dropna(subset=["Customer ID"])

# Remove negative or zero Quantity
df = df[df["Quantity"] > 0]

# Remove negative or zero Price
df = df[df["Price"] > 0]

# Create Sales column
df["Sales"] = df["Quantity"] * df["Price"]

print("\nAfter Cleaning:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv(
    "data/cleaned_retail.csv",
    index=False
)

print("\ncleaned_retail.csv created successfully")