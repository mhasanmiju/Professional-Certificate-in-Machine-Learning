# Pandas/17_value_replace_map.py
import pandas as pd

data = {'Name': ['Miju', 'Alice', 'Bob', 'Charlie'], 'Department': ['Engineer','HR', 'IT', 'Finance']}
df = pd.DataFrame(data)
dept_update = { 'Engineer': 1,'HR': 2, 'IT': 3, 'Finance': 4}
print(f"Old df: \n{df}")
df["Dept_code"] = df["Department"].map(dept_update)
print(f"New df: \n{df}")