# Pandas/11_Rolling_window.py
import pandas as pd
date_range = pd.date_range(start='2024-02-25', periods= 10, freq="D")
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)
print(f"Data before Rolling: \n{df}")
df["Rolling_Mean"] = df.rolling(window=4).mean()
print(f"Data After Rolling: \n{df}")