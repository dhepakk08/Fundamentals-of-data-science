import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

df = pd.read_csv("data.csv").dropna(subset=["feedback"])
words = re.findall(r"\b[a-zA-Z]+\b", " ".join(df["feedback"].astype(str)).lower())
counts = Counter(w for w in words if w not in ENGLISH_STOP_WORDS)
n = int(input("How many top words should be displayed? "))
top = counts.most_common(max(1, n))
print(top)
if top:
    labels, values = zip(*top)
    plt.figure(figsize=(max(8, len(labels)*.45), 4))
    plt.bar(labels, values); plt.title(f"Top {len(top)} words in feedback")
    plt.ylabel("Frequency"); plt.xticks(rotation=55, ha="right"); plt.tight_layout(); plt.show()
