# 33_NumPy_IndexingWithWhere.py
import numpy as np

# Creating an array
array = np.array([[10, 20, 30, 40, 50], [5, 7, 9, 25, 99]])

# Using np.where to find indices where elements are greater than 25
indices = np.where(array > 25) #1D
result = np.where(array > 25, array, 0) # 2D

print('Indices where elements > 25:', indices)
print('Values where elements > 25:', array[indices])
print('Values where elements > 25:', result)

