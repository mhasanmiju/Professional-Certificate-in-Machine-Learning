# Pandas/3_lambda.py
import pandas as pd

data = {"name" : ["Miju", "Riju","Hasan", "Hussain"], "Scores": [80, 85, 95, 90]}

df = pd.DataFrame(data)

df["Bonus_Scores"] = df["Scores"].apply(lambda x: x+7 if x < 90 else x)

print(f"Updated DataFrame: \n{df}") 