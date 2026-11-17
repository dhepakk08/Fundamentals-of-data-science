import pandas as pd

df = pd.read_csv("quarterly_sales.csv").sort_values("Quarter")
total = df["Sales"].sum()
q1 = df.loc[df["Quarter"] == 1, "Sales"].sum()
q4 = df.loc[df["Quarter"] == 4, "Sales"].sum()
increase = ((q4 - q1) / q1 * 100) if q1 else float("nan")
print(f"Year total sales: {total:,.2f}")
print(f"Q1 to Q4 percentage change: {increase:.2f}%")
