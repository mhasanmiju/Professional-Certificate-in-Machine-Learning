# Pandas/2_MultiIndex.py
import pandas as pd
array = [['a', 'a', 'b', 'b'], [2025,2024,2024,2025]]
index = pd.MultiIndex.from_arrays(array, names = ("Category", "Year"))
data = [2000,300,5000,4000]
df = pd.DataFrame(data, index= index, columns=["Sales"])
print(f"Data Frame: \n{df}")

# Accessing data in a MultiIndex DataFrame
sales_2025 = df.xs(2024, level='Year')
group = df.groupby("Year").agg(Total_Sales = ("Sales","sum") , Average_sale = ("Sales","mean"))
print(f"Sales in 2024: {sales_2025}")
print(f"Average Sales: \n{group}")