# Pandas/8_Time_resample.py
import pandas as pd
data_range =pd.date_range(start='2024-02-13', periods= 15, freq="D")
data = {
    'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400, 450, 500, 350, 600, 550]
}

df = pd.DataFrame(data, index= data_range)
weakly_sales = df.resample('W').sum()

print(f'data frame: \n{df}')
print(f'Weakly Sales: \n{weakly_sales}')
