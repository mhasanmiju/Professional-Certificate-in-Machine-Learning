# Code_Exam/numpy_replace.py
# Create a 1-dimensional array of integers from 1 to 50.
# Replace all multiples of 5 with -1 and print the resulting array.

import numpy as np

array = np.arange(1, 51)
print(f"Original Array: {array}")
array[array % 5 == 0] = -1
print(f"Replaced Array: {array}")