import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned/products_cleaned.csv")

print("\n===== DATA PREVIEW =====")
print(df.head())

# ===== All Products Sheet =====
#all_products = df   # ← Full product list

# ===== Analysis =====

total_products = len(df)
print (total_products)
avg_price = df["price"].mean()
avg_rating = df["rating"].mean()

expensive = df.sort_values("price", ascending=False)[["product_name","price"]]
cheap = df.sort_values("price")[["product_name","price"]]
price_dist = df["price_bucket"].value_counts()
top_rated = df.sort_values("rating", ascending=False)[["product_name","rating"]]

# ===== Summary Table =====
summary = pd.DataFrame({
    "Metric":["Total Products", "Average Price", "Average Rating"],
    "Value":[total_products, avg_price, avg_rating]
})

# ===== Save Excel File =====
with pd.ExcelWriter("analysis_output.xlsx", engine="openpyxl") as writer:

    # 1st Sheet → All Products
    df.to_excel(
        writer,
        sheet_name="Total Products",
        index=False        
    )

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    expensive.to_excel(
        writer,
        sheet_name="Expensive Products",
        index=False
    )

    cheap.to_excel(
        writer,
        sheet_name="Cheap Products",
        index=False
    )

    price_dist.to_excel(
        writer,
        sheet_name="Price Distribution"
    )

    top_rated.to_excel(
        writer,
        sheet_name="Top Rated",
        index=False
    )


print ('\nExcel File Created Successfully!');
print (total_products)