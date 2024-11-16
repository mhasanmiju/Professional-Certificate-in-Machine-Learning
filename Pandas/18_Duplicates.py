# Pandas/18_Duplicates.py
import pandas as pd

data = {'ID': [1, 2, 2, 3, 4, 4], 'Value': [10, 20, 20, 30, 40, 40]}
df = pd.DataFrame(data)
print(f"Original Df: \n{df}")

duplicates = df[df.duplicated()]
print(f"Duplicates rows: \n{duplicates}")

remove_duplicates = df.drop_duplicates()

print(f"Removed duplicates data: \n{remove_duplicates}")

# Remove duplicate rows and reset the index
df_no_duplicates = df.drop_duplicates().reset_index(drop=True)
print(f"DataFrame without duplicates (index reset): \n{df_no_duplicates}")