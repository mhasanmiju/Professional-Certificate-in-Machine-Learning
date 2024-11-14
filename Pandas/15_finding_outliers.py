# Pandas/15_finding_outliers.py
import pandas as pd
import numpy as np

data = {"Values": [1,5,9,11,12,20,25,30,35,34,33,23,24,35,55,75,100]}
df= pd.DataFrame(data)

print(f"DataFrame: \n{df}")
q1 = df["Values"].quantile(.25)
q3 = df["Values"].quantile(.75)
IQR = q3 - q1

outliers = df[(df["Values"] < (q1 - 1.5 * IQR)) | (df["Values"] > (q3 + 1.5 * IQR))]
df_without_outliers = df[(df["Values"] >= (q1 - 1.5 * IQR)) & (df["Values"] <= (q3 + 1.5 * IQR))]

print(f"Outliers: \n{outliers}")
print(f"Without Outliers: \n{df_without_outliers}")