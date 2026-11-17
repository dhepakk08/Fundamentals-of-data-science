import pandas as pd

df = pd.read_csv("fuel_efficiency.csv")
df["highway_mpg"] = pd.to_numeric(df["highway_mpg"], errors="coerce")
print(f"Average highway fuel efficiency: {df['highway_mpg'].mean():.2f} mpg")
models = df.dropna(subset=["highway_mpg"]).drop_duplicates(["make", "model"])
print("Enter two model names exactly as shown below:")
print(models[["make", "model", "highway_mpg"]].head(10).to_string(index=False))
first = input("First model: ").strip()
second = input("Second model: ").strip()
def lookup(model):
    row = models[(models["model"].str.casefold() == model.casefold())]
    return float(row.iloc[0]["highway_mpg"]) if not row.empty else None
a, b = lookup(first), lookup(second)
if a is None or b is None: print("Model not found; use a model shown in the table.")
else: print(f"Efficiency change from first to second: {(b-a)/a*100:.2f}%")
