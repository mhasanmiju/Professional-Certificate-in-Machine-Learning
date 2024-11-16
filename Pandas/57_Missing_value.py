# Pandas/57_Missing_value.py
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Sales': [200, np.nan, 300, np.nan, 500],
    'Profit': [50, 60, np.nan, 80, np.nan]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Forward fill to propagate the last valid value
df_ffill = df.fillna(method='ffill')

print("\nDataFrame after forward fill (ffill):")
print(df_ffill)

# Backward fill to propagate the next valid value
df_bfill = df.fillna(method='bfill')

print("\nDataFrame after backward fill (bfill):")
print(df_bfill)
# ffill (Forward Fill): Fills NaN values with the last valid (non-NaN) value above it.

# bfill (Backward Fill): Fills NaN values with the next valid (non-NaN) value below it.