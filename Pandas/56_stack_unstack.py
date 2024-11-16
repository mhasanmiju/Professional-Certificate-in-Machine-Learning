# Pandas/56_stack_unstack.py

import pandas as pd

# Create a sample DataFrame with MultiIndex
data = {
    'Math': [85, 89, 92],
    'Science': [78, 90, 84],
    'English': [91, 85, 88]
}
df = pd.DataFrame(data, index=['Alice', 'Bob', 'Charlie'])

print("Original DataFrame:")
print(df)

stacked = df.stack()

print("\nStacked DataFrame:")
print(stacked)

unstacked = stacked.unstack()

print("\nUnstacked DataFrame:")
print(unstacked)

