import pandas as pd

df = pd.read_csv("orders.csv")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print("Orders per customer:")
print(df.groupby("customer_id")["order_id"].nunique().sort_values(ascending=False))
print("\nAverage quantity by product:")
print(df.groupby("product_name")["quantity"].mean().round(2).sort_values(ascending=False))
print("\nEarliest order:", df["order_date"].min())
print("Latest order:", df["order_date"].max())
