
# 22_NumPy_BooleanIndexing.py
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Boolean indexing
odd_numbers = array[array % 2 == 1]

print('Original Array:', array)
print('Odd Numbers:', odd_numbers)
