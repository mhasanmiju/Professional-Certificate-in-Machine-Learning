# 17_Multidimensinal_slicing.py
import numpy as np
array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"Original Array: {array}")

sliced_array = array[:, :, 1:3]
print(f"Sliced Array: {sliced_array}")