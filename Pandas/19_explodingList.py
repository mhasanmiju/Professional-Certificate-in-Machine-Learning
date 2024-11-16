# Pandas/19_explodingList.py

import pandas as pd

# Creating a DataFrame with lists in a column
data = {'ID': [1, 2], 'Hobbies': [['Reading', 'Swimming'], ['Running', 'Cycling']]}
df = pd.DataFrame(data)
print(f"Original df: \n{df}")
# Exploding the 'Hobbies' column
exploded_df = df.explode('Hobbies')

print('DataFrame after Exploding Lists:\n', exploded_df)