# Pandas/10_Cut_function_custom_column.py
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)
print(df)
df["Performance"] = pd.cut(df["Score"], bins =[0, 60, 70, 80, 90, 100], labels=["Poor","Average","Good", "Better", "Best"])
print(f"Updated DF: \n{df}")
