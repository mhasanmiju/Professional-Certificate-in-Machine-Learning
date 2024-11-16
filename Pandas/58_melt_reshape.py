# Pandas/58_melt_reshape.py
import pandas as pd
data = {
    'Region': ['North', 'South', 'East'],
    'Jan': [100, 200, 150],
    'Feb': [110, 210, 160],
    'Mar': [120, 220, 170]
}
df = pd.DataFrame(data)

# Melt the data
melted = pd.melt(df, id_vars=['Region'], var_name='Month', value_name='Sales')

print(melted)
