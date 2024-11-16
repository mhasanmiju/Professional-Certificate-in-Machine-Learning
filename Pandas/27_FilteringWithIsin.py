
# Example 27: Pandas/27_FilteringWithIsin.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Filtering with isin
filtered_df = df[df['City'].isin(['NY', 'SF'])]

print('Filtered DataFrame with isin Method:\n', filtered_df)
