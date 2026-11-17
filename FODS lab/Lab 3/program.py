import pandas as pd

df = pd.read_csv("house_prices.csv")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["sale_price"] = pd.to_numeric(df["sale_price"], errors="coerce")
eligible = df.loc[df["bedrooms"] > 4, "sale_price"].dropna()
print("Houses with more than 4 bedrooms:", len(eligible))
print("Average sale price:", round(eligible.mean(), 2) if len(eligible) else "No matching houses")
