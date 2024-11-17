import pandas as pd

# Create a DataFrame
data = {'A': [1, 3, 4, 2], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
print("\n",df)
print("--------------")
# Add a new row
df.loc[4] = [9, 10]
print("\n",df)
print("--------------")
# Add a new column
df.loc[:, 'C'] = [11, 20, 30, 40, 50]
print("\n",df)

print("--------------")
# Find the sum of columns 'A' and 'B' where 'A' > 2
df.loc[df['A'] < 2, ['A', 'B']] = [df['A'].min(), df['B'].max()]
print(df)