# 16_broadcasting.py
import numpy as np

# Creating an array
array = np.array([10, 20, 30])

# Broadcasting: Adding a scalar to an array
result = array + 10

print('Original Array:', array)
print('Array after Broadcasting:', result)