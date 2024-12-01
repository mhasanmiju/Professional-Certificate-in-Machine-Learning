import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example dataset
tips = sns.load_dataset("tips")  # Built-in dataset in Seaborn

# Violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True, palette="muted")

# Adding titles and labels
plt.title("Distribution of Total Bill by Day and Gender", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill ($)", fontsize=12)
plt.show()
