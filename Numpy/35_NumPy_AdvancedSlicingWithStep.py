# 35_NumPy_AdvancedSlicingWithStep.py
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Slicing every second element in rows and columns
result = array_2d[::2, 1::2]

print('Advanced Sliced Array with Step:\n', result)
