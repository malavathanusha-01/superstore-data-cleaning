import pandas as pd

# ---------------------------
# 1. Load Dataset (with encoding fix)
# ---------------------------
file_path = "Sample - Superstore.csv"

try:
    df = pd.read_csv(file_path, encoding='latin1', low_memory=False)
    print("✅ File loaded successfully!")
except FileNotFoundError:
    print("❌ File not found. Check file name/path.")
    exit()

# ---------------------------
# 2. Basic Info
# ---------------------------
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 First 5 Rows:")
print(df.head())

# ---------------------------
# 3. Check Missing Values
# ---------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# Fill missing Postal Code (if any)
if 'Postal Code' in df.columns:
    df['Postal Code'] = df['Postal Code'].fillna(0)

# ---------------------------
# 4. Remove Duplicates
# ---------------------------
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"\n🔹 Duplicates removed: {before - after}")

# ---------------------------
# 5. Fix Data Types
# ---------------------------
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

if 'Ship Date' in df.columns:
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# ---------------------------
# 6. Standardize Text Columns
# ---------------------------
text_cols = ['Country', 'Category', 'Sub-Category', 'City', 'State']

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

# ---------------------------
# 7. Feature Engineering
# ---------------------------

# Delivery Days
if 'Order Date' in df.columns and 'Ship Date' in df.columns:
    df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Profit Margin
if 'Profit' in df.columns and 'Sales' in df.columns:
    df['Profit Margin'] = df['Profit'] / df['Sales']

# ---------------------------
# 8. Handle Outliers (optional)
# ---------------------------
if 'Sales' in df.columns:
    upper_limit = df['Sales'].quantile(0.99)
    df = df[df['Sales'] < upper_limit]
    print(f"\n🔹 Removed outliers above: {upper_limit}")

# ---------------------------
# 9. Save Cleaned Data
# ---------------------------
output_file = "cleaned_superstore.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Cleaned data saved as: {output_file}")

# ---------------------------
# 10. Final Summary
# ---------------------------
print("\n🔹 Final Dataset Shape:", df.shape)