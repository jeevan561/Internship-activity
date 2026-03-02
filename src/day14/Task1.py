import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print("Original Dataset:\n")
print(df)

#Label Encoding
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("\nAfter Label Encoding (Transmission):\n")
print(df)

#One-Hot Encoding
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter One-Hot Encoding (Color):\n")
print(df)

print("\nFinal Dataset Shape:", df.shape)
