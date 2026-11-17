import pandas as pd
from math import sqrt
from scipy.stats import norm

df = pd.read_csv("ab_test.csv")
groups = {name: frame["Converted"].astype(int) for name, frame in df.groupby("Design")}
a, b = groups["A"], groups["B"]
p_a, p_b = a.mean(), b.mean()
p_pool = (a.sum()+b.sum())/(len(a)+len(b))
se = sqrt(p_pool*(1-p_pool)*(1/len(a)+1/len(b)))
z = (p_a-p_b)/se if se else 0.0
p_value = 2*(1-norm.cdf(abs(z)))
print(f"Design A conversion: {p_a:.2%} (n={len(a)})")
print(f"Design B conversion: {p_b:.2%} (n={len(b)})")
print(f"Two-sided two-proportion z test: z={z:.3f}, p={p_value:.4g}")
print("Statistically significant at 0.05:", p_value < 0.05)
