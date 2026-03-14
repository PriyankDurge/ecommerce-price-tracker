import pandas as pd

df = pd.read_csv("../data/raw/products_raw.csv")

df["price"] = df["price"].astype(str) #add
df["price"] = df["price"].str.replace("₹","") #add 
df["price"] = df["price"].str.replace(",","") #add

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce")

df.drop_duplicates(subset=["product_name"], inplace=True)

df["price_bucket"] = pd.cut(
    df["price"],
    bins=[0, 30000, 60000, 100000, 200000],
    labels=["Low", "Mid", "High", "Premium"]
)

df.to_csv("../data/cleaned/products_cleaned.csv", index=False)

print("Cleaning completed!")