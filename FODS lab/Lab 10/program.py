import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales.csv", parse_dates=["month"]).sort_values("month")
fig, axes = plt.subplots(1, 2, figsize=(13, 4))
axes[0].plot(df["month"], df["sales"], marker="o"); axes[0].set_title("Monthly Sales — Line Plot")
axes[1].bar(df["month"].dt.strftime("%Y-%m"), df["sales"]); axes[1].set_title("Monthly Sales — Bar Plot"); axes[1].tick_params(axis="x", rotation=70)
for ax in axes: ax.set_ylabel("Sales"); ax.grid(axis="y", alpha=.25)
plt.tight_layout(); plt.show()
