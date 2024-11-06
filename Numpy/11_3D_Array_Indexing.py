#11_3D_Array_Indexing.py

import numpy as np

array = np.array([[[1, 3, 5], [7, 9, 11]], [[2, 4, 6], [8, 10, 12]]])

# Accessing elements in a 3D array
element = array[1, 1, 2]  # Accessing the element at [1, 1, 2]
# Slicing in 3D
slice_3d = array[:, 0, :]

print(f"Accessed Element: {element}")
print(f"Sliced Element: {slice_3d}")