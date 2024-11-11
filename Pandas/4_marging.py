# Pandas/4_marging.py
import pandas as pd
df1 = pd.DataFrame({"ID": [1,2,3],"name" :["Miju", "Riju", "Hasan"]})
df2 = pd.DataFrame({"emp_Id": [1,2,4], "Department": ["Engineer", "Scientist", "HR"]})
df3 = pd.merge(df1,df2, left_on="ID", right_on="emp_Id", how="outer")

print(f"DataFrame 1: \n{df1}")
print(f"DataFrame 2: \n{df2}")
print(f"Updated DataFrame: \n{df3}")