# Pandas/55_Multi_index_Pivot.py
import pandas as pd

# Creating a DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'], 'Type': ['Online', 'Store', 'Online', 'Store'], 'Sales': [200, 250, 300, 350]}
df = pd.DataFrame(data)

pivot_data = df.pivot(index="Date", columns=["City", "Type"], values="Sales")

print(f"Pivot Table: \n{pivot_data}")