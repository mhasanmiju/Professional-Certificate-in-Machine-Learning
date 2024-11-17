# Pandas/53_Custom_BusinessDay.py
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

# Define a custom business day frequency for Friday and Saturday
friday_saturday = CustomBusinessDay(weekmask='Fri Sat')

# Creating a time series with Fridays and Saturdays only
date_range = pd.date_range(start='2023-01-01', periods=10, freq=friday_saturday)
data = {'Sales': range(10)}
df = pd.DataFrame(data, index=date_range)

print('Time Series DataFrame with Fridays and Saturdays:\n', df)
