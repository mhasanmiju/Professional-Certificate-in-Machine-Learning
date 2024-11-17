
# Example 42: Pandas/42_RollingWithCustomFunctions.py

import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data, index=date_range)

# Applying a custom function with rolling()
df['Rolling Sum'] = df['Values'].rolling(window=3).apply(lambda x: x.sum() if x.sum() > 70 else 0)

print('DataFrame with Custom Rolling Sum:\n', df)
