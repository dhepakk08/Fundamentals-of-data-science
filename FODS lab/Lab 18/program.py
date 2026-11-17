import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("bodyfat_18_adults.csv")
for col in ["Age", "BodyFat_Percent"]:
    x = pd.to_numeric(df[col], errors="coerce").dropna()
    print(f"{col}: mean={x.mean():.2f}, median={x.median():.2f}, sample SD={x.std():.2f}")
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0,0].boxplot(df["Age"].dropna()); axes[0,0].set_title("Age boxplot")
axes[0,1].boxplot(df["BodyFat_Percent"].dropna()); axes[0,1].set_title("Body fat boxplot")
axes[1,0].scatter(df["Age"], df["BodyFat_Percent"]); axes[1,0].set(xlabel="Age", ylabel="Body fat (%)", title="Age vs body fat")
stats.probplot(df["BodyFat_Percent"].dropna(), dist="norm", plot=axes[1,1]); axes[1,1].set_title("Q-Q plot: body fat")
plt.tight_layout(); plt.show()
