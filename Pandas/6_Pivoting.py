# Pandas/6_Pivoting.py
import pandas as pd

data = data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'],
        'Sales': [200, 250, 300, 400]}

df = pd.DataFrame(data)

pivot_df = df.pivot(index="Date", columns="City", values="Sales")

print(f"Pivot Data: \n{pivot_df}")