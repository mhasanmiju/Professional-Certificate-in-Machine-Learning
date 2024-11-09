
# 30_NumPy_SplittingArrays.py
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Splitting the array into three parts
split_arrays = np.array_split(array, 3)

print(f'Split Arrays: {split_arrays}')
