# 34_NumPy_MeshgridCreation.py
import numpy as np

# Creating 1D arrays
x = np.array([1, 3, 5])
y = np.array([7, 9, 11])

# Creating a meshgrid
X, Y = np.meshgrid(x, y)

print('Meshgrid X:\n', X)
print('Meshgrid Y:\n', Y)
