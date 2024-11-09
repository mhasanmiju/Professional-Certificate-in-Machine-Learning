
# Example 14: NumPy - Using Ellipsis (...) in Indexing
import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Using ellipsis to select all elements along specific axes
result = array_3d[..., 1]  # Selecting the second column in each 2D slice

print('Result using Ellipsis (...):\n', result)

# general way
sliced_3d = array_3d[ : , : , 1 :  ]
print(f"sliced: \n{sliced_3d}")

# in original shaped
# Create an output array with the same shape as array_3d, initialized to 0
result = np.zeros_like(array_3d)
# Place the sliced values in the corresponding position in the result array
result[:, :, 1:] = sliced_3d
print("Result with Zeros in Original Shape:\n", result)