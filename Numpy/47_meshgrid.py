# 47_meshgrid.py
import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Creating meshgrid for advanced indexing
X, Y = np.meshgrid(x, y)
indices = np.vstack([X.ravel(), Y.ravel()])

print('Indices for Meshgrid Advanced Indexing:\n', indices)