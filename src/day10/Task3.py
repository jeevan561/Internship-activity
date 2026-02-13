import pandas as pd

data = {
    "Location": [
        " New York",
        "new york",
        "NEW YORK ",
        "Los Angeles",
        " los angeles ",
        "LOS ANGELES",
        " Chicago ",
        "chicago",
        "CHICAGO "
    ]
}

df = pd.DataFrame(data)

print("Unique values BEFORE cleaning:")
print(df["Location"].unique())

print("\nTotal unique BEFORE:", df["Location"].nunique())

df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.title()

print("\nUnique values AFTER cleaning:")
print(df["Location"].unique())

print("\nTotal unique AFTER:", df["Location"].nunique())

print("\nGrouped Counts:")
print(df.groupby("Location").size())
