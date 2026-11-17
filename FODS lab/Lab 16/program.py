from collections import Counter
import pandas as pd
import re

df = pd.read_csv("customer_reviews.csv").dropna(subset=["review"])
words = re.findall(r"\b[\w']+\b", " ".join(df["review"].astype(str)).lower())
counts = Counter(words)
print("Review count:", len(df), "| unique words:", len(counts))
print("Top 25 words:")
for word, count in counts.most_common(25): print(f"{word}: {count}")
