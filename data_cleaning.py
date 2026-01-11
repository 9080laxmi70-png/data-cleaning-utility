import pandas as pd

# Read raw data
df = pd.read_csv("raw_data.csv")

log = []

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
log.append("Standardized column names")

# Remove duplicate rows
df = df.drop_duplicates()
log.append("Removed duplicate rows")

# Convert data types
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Handle missing values
df["age"].fillna(df["age"].median(), inplace=True)
df["salary"].fillna(df["salary"].mean(), inplace=True)
log.append("Handled missing values")

# Fix date column
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
log.append("Converted join_date to datetime")

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Save log
with open("cleaning_log.txt", "w") as f:
    for item in log:
        f.write(item + "\n")

print("Data cleaning completed")
