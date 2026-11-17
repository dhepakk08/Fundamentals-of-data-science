import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales.csv", parse_dates=["month"]).sort_values("month").reset_index(drop=True)
x = np.arange(len(df)); y = df["sales"].to_numpy(dtype=float)
coef = np.polyfit(x, y, 1) if len(df) >= 2 else [0, y[0]]
trend = np.polyval(coef, x)
next_value = float(np.polyval(coef, len(df)))
fig, axes = plt.subplots(1, 3, figsize=(16, 4))
axes[0].plot(df["month"], y, marker="o"); axes[0].set_title("Sales over time")
axes[1].scatter(df["month"], y, label="Observed"); axes[1].plot(df["month"], trend, color="red", label="Linear trend"); axes[1].legend(); axes[1].set_title("Scatter and trend")
axes[2].bar(df["month"].dt.strftime("%Y-%m"), y); axes[2].tick_params(axis="x", rotation=70); axes[2].set_title("Monthly sales")
for ax in axes: ax.set_ylabel("Sales"); ax.grid(axis="y", alpha=.2)
plt.tight_layout(); plt.show()
print(f"Simple linear-trend estimate for the next month (not a validated forecast): {next_value:,.2f}")
