# 44_Indexing_with_take.py
import numpy as np

# Creating an array
array = np.array([100, 50, 60, 4, 250])

# Using np.take to select elements at specific indices
indices = [0, 2, 4]
result = np.take(array, indices)

print('Selected Elements using np.take:', result)