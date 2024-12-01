
# Pandas/46_WorkingWithTimeZones.py
import pandas as pd

# Creating a time series with a timezone
date_range = pd.date_range(start='2023-01-01', periods=5, freq='D', tz='UTC')
data = {'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data, index=date_range)

# Converting to a different timezone
df = df.tz_convert('US/Eastern')

print('Time Series DataFrame with Time Zones:\n', df)
