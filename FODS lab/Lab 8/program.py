import pandas as pd

df = pd.read_csv("product_sales.csv")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
latest = df["order_date"].max()
month = df[df["order_date"].dt.to_period("M") == latest.to_period("M")]
top = month.groupby("product_name")["quantity"].sum().nlargest(5)
print("Top products in the latest month available in this historical file:")
print(top)
