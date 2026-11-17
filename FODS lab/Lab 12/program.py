import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_weather.csv").sort_values("Month")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(df["Month"], df["temperature"], marker="o"); axes[0].set_title("Monthly Temperature")
axes[1].scatter(df["Month"], df["rainfall"], color="teal"); axes[1].set_title("Monthly Rainfall")
for ax in axes: ax.set_xlabel("Month"); ax.grid(alpha=.25)
axes[0].set_ylabel("Temperature"); axes[1].set_ylabel("Rainfall")
plt.tight_layout(); plt.show()
