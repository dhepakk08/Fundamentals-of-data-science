import pandas as pd

df = pd.read_csv("post_likes.csv")
print("Frequency distribution of likes per post:")
print(df["likes"].value_counts().sort_index())
