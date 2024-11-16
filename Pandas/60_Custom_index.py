# Pandas/60_Custom_index.py
import pandas as pd
import numpy as np

# Create a MultiIndex
index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 2)],
    names=['Group', 'Subgroup']
)

# Create a DataFrame
data = pd.DataFrame(
    {
        'Value1': [10, 20, 30, 40],
        'Value2': [100, 200, 300, 400]
    },
    index=index
)

print("MultiIndex DataFrame:")
print(data)
