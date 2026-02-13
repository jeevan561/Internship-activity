import pandas as pd
data = {
    "Price": ["$100", "$250", "$300", "$150"],
    "Date": ["2026-02-01", "2026-02-02", "2026-02-03", "2026-02-04"]
}

df = pd.DataFrame(data)

print("Initial Data Types:")
print(df.dtypes)
print("\nDataFrame Before Cleaning:")
print(df)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nFinal Data Types:")
print(df.dtypes)

print("\nDataFrame After Cleaning:")
print(df)

print("\nAverage Price:", df["Price"].mean())

df.set_index("Date", inplace=True)
daily_average = df.resample("D").mean()

print("\nDaily Average (Time-Series Ready Data):")
print(daily_average)
