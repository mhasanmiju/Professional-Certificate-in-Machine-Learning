# 18_Modifynig_array_values.py
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Modifying values at specific indices
array[[0, 3]] = [-60, 999]

print('Modified Array:', array)
