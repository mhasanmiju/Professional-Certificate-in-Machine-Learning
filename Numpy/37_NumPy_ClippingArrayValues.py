
# 37_NumPy_ClippingArrayValues.py
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Clipping values to be between 2 and 6
clipped_array = np.clip(array, 2, 6)

print('Original Array:', array)
print('Clipped Array:', clipped_array)
