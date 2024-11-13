# Pandas/7_melting_pivoting.py
import pandas as pd
df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Carol"],
    "Math": [85, 78, 92],
    "English": [90, 85, 95],
    "Science": [88, 82, 94],
    "History": [92, 88, 90]
})

# Melt without specifying value_vars; it will melt all columns except 'Student'
melted_df = pd.melt(df, id_vars=["Student"], var_name="Subject", value_name="Score")
print(melted_df)

# Melt only the 'Math' and 'Science' columns, keeping 'Student' as id_vars
melted_df = pd.melt(df, id_vars=["Student"], value_vars=["Math", "Science"], var_name="Subject", value_name="Score")
print("\nMelted DataFrame with Math and Science:\n", melted_df)

