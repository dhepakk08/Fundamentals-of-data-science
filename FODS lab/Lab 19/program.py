import pandas as pd
from scipy import stats

df = pd.read_csv("blood_pressure.csv")
for group, values in df.groupby("Group")["Reduction"]:
    x = pd.to_numeric(values, errors="coerce").dropna()
    mean = x.mean(); se = stats.sem(x); critical = stats.t.ppf(0.975, len(x)-1)
    low, high = mean-critical*se, mean+critical*se
    print(f"{group}: n={len(x)}, mean reduction={mean:.2f} mmHg, 95% CI=({low:.2f}, {high:.2f})")
