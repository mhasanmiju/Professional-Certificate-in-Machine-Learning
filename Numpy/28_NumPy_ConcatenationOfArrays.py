
# Example 15: NumPy - Concatenation of Arrays
import numpy as np

# Creating 2D arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Concatenating along rows (axis=0)
concatenated_array_rows = np.concatenate((array1, array2), axis=0)
print(f'Concatenated along rows:\n{concatenated_array_rows}\n')

# Concatenating along columns (axis=1)
concatenated_array_columns = np.concatenate((array1, array2), axis=1)
print(f'Concatenated along columns:\n{concatenated_array_columns}')

