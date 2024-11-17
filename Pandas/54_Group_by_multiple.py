# Pandas/54_Group_by_multiple.py
import pandas as pd

# Creating a DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)
group_df = df.groupby("Category")["Value"].agg(["sum","mean","max","min"])
print(f"Statistical_measure: \n{group_df}")