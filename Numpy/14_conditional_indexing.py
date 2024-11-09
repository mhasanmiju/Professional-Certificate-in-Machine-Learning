# Numpy/14_conditional_indexing.py
import numpy as np

# Creating an array
array = np.array([11, 20, 30, 45, 50, 61])

# Setting elements that satisfy a condition
array[array % 2 == 0] = -2  # Set even numbers to -1

print('Array after Conditional Indexing:', array)