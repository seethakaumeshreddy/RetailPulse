import pandas as pd

# Load Excel file
file_path = "data/online_retail_II.xlsx"

# Load both sheets
df1 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010",
    engine="openpyxl"
)

df2 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011",
    engine="openpyxl"
)
# Combine both datasets
df = pd.concat([df1, df2], ignore_index=True)

print("Dataset Loaded Successfully")
print()

print("Rows and Columns:")
print(df.shape)

print()
print("Column Names:")
print(df.columns)

print()
print("First 5 Rows:")
print(df.head())

# Save combined file
df.to_csv("data/combined_retail.csv", index=False)

print()
print("combined_retail.csv created successfully")