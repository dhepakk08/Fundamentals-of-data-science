import pandas as pd

df = pd.read_csv("customer_purchases.csv", parse_dates=["purchase_date"])
df = df[df["made_purchase"].eq(1)].copy()
latest_month = df["purchase_date"].max().to_period("M")
recent = df[df["purchase_date"].dt.to_period("M") == latest_month]
print(f"Age frequency for purchasers in latest data month ({latest_month}):")
print(recent["age"].value_counts().sort_index())
