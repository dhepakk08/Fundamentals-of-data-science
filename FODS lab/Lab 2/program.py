import pandas as pd

df = pd.read_csv("product_prices.csv")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Quantity_Sold"] = pd.to_numeric(df["Quantity_Sold"], errors="coerce")
sold = df.dropna(subset=["Price", "Quantity_Sold"]).query("Quantity_Sold > 0")
print(f"Average listed product price for sold items: {sold['Price'].mean():.2f}")
