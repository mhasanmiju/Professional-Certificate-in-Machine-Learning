import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])

# Accessing individual elements
element = array_2d[2, 2]  # Accessing element at row 3, column 3

# Slicing rows and columns
row_slice = array_2d[0, :]  # First row all column values
column_slice = array_2d[:, 1] #Second column all row values
print(f"Full Array: {array_2d}")
print(f"Aarry 3rd row's 3rd column element: {element}")
print(f"Sliced Row: {row_slice}")
print(f"Sliced Column: {column_slice}")