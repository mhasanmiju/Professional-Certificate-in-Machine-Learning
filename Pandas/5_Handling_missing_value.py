# Pandas/5_Handling_missing_value.py
import pandas as pd
import numpy as np

data = {"Name": ["Miju", "Nasim", "Pranto", np.nan], "Age":[26, np.nan, 27, 29]}
df = pd.DataFrame(data)
print(f"With missing values: \n{df}")
df["Name"].fillna("Unknown", inplace = True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(f"Without missing values: \n{df}")