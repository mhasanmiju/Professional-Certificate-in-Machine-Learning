# Pandas/22_Create_dummy.py
import pandas as pd
data = {'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)
dummy = pd.get_dummies(df["City"], prefix="City").astype(int)
print(f"Dummiy: {dummy}")