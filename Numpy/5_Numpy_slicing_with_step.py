# NumPy - Slicing with Step

import numpy as np

# Creating an array
array = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# Slicing
step_slice = array[::2]  # Every second element
print(f"Sliced Array with Step: {step_slice}")
