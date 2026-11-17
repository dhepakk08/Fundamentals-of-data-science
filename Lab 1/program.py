import pandas as pd
import numpy as np

df = pd.read_csv("student_scores.csv")
subjects = ["Math", "Science", "English", "History"]
scores = df[subjects].to_numpy(dtype=float)
means = scores.mean(axis=0)
print("Average score by subject:")
for subject, mean in zip(subjects, means): print(f"{subject}: {mean:.2f}")
print("Highest average:", subjects[int(np.argmax(means))])
