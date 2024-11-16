# Pandas/59_data_shift.py

import pandas as pd
import numpy as np
index = pd.date_range(start='2024-03-23', periods= 10, freq="M")
data = {
    'Sales': np.random.randint(100, 500, size=10),
    'Profit': np.random.randint(20, 100, size=10)}
df = pd.DataFrame(data)
print(data)
# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Create lagged columns (shifted by 1 month)
df['Previous_Month_Sales'] = df['Sales'].shift(1)
df['Previous_Month_Profit'] = df['Profit'].shift(1)

# Display the DataFrame
print("Data with lagged columns:")
print(df)
