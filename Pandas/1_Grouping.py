# Pandas/1_Grouping.py
import pandas as pd
data = {
    "Category" : ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],
    "Values" : [30, 40, 50, 20, 30, 50, 60, 30]
}

df= pd.DataFrame(data)
group = df.groupby("Category").agg(Total_Value = ("Values", "sum"), Agerage_Value = ("Values","mean"))
print(f"Data Frame: \n{df}")
print(f"Agrregation: \n{group}")