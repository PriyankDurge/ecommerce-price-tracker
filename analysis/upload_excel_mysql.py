# import pandas as pd
# from sqlalchemy import create_engine

# # Load cleaned data
# df = pd.read_csv("../data/cleaned/products_cleaned.csv")

# # Connect MySQL
# engine = create_engine(
# "mysql+pymysql://root:Mysql@5@localhost/ecommerce_tracker"
# )

# # Upload data
# df.to_sql(
# "products",
# engine,
# if_exists="append",
# index=False
# )


# print("Data uploaded successfully")

import pandas as pd
from sqlalchemy import create_engine

# Connect MySQL
engine = create_engine("mysql+pymysql://root:Mysqlpass@localhost/ecommerce_tracker")

# Excel file path
file_path = "analysis_output.xlsx"

# Load sheets
total_products = pd.read_excel(file_path,sheet_name="Total Products")
summary = pd.read_excel(file_path,sheet_name="Summary")
expensive = pd.read_excel(file_path,sheet_name="Expensive Products")
cheap = pd.read_excel(file_path,sheet_name="Cheap Products")
top_rated = pd.read_excel(file_path,sheet_name="Top Rated")
price_dist = pd.read_excel(file_path,sheet_name="Price Distribution")

# Upload to MySQL
total_products.to_sql("total_products", engine,if_exists="replace", index=False)
summary.to_sql("summary", engine,if_exists="replace", index=False)
expensive.to_sql("expensive_products", engine, if_exists="replace", index=False)
cheap.to_sql("cheap_products", engine, if_exists="replace", index=False)
top_rated.to_sql("top_rated", engine, if_exists="replace", index=False)
price_dist.to_sql("price_distribution", engine, if_exists="replace", index=False)

print("Excel Uploaded Successfully")

# Fetch 5 rows from MySQL
query = "SELECT * FROM total_products LIMIT 5"
df = pd.read_sql(query, engine)

print("\nFirst 5 rows from MySQL:")
print(df)