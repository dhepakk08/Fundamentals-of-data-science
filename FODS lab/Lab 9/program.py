import pandas as pd

df = pd.read_csv("properties.csv")
df["listing_price"] = pd.to_numeric(df["listing_price"], errors="coerce")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["area_sqft"] = pd.to_numeric(df["area_sqft"], errors="coerce")
print("Average listing price by location:")
print(df.groupby("furnishingstatus")["listing_price"].mean().round(2))
print("Properties with more than four bedrooms:", int((df["bedrooms"] > 4).sum()))
print("Largest property:")
print(df.loc[df["area_sqft"].idxmax()])
