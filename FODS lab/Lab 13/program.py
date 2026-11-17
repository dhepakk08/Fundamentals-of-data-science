from collections import Counter
import re

with open("sample_text.txt", encoding="utf-8") as f: text = f.read().lower()
words = re.findall(r"\b[\w']+\b", text)
freq = Counter(words)
print("Total words:", len(words)); print("Unique words:", len(freq))
print("Most common words:")
for word, count in freq.most_common(20): print(f"{word}: {count}")
