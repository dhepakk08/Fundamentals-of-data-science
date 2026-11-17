import pandas as pd

df = pd.read_csv("grocery_items.csv")
discount_rate = float(input("Discount percentage: ")) / 100
tax_rate = float(input("Tax percentage: ")) / 100
subtotal = (df["price"] * df["quantity"]).sum()
discount = subtotal * discount_rate
taxable = subtotal - discount
tax = taxable * tax_rate
print(f"Subtotal: {subtotal:.2f}; discount: {discount:.2f}; tax: {tax:.2f}")
print(f"Total due: {taxable + tax:.2f}")
