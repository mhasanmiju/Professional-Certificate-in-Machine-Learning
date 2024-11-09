
# 26_NumPy_UniqueElementsAndCounting.py
import numpy as np

# Creating a 2D array with duplicate values
array = np.array([[1, 2, 2], [3, 4, 4], [4, 5, 5]])

# Finding unique elements and their counts
unique_elements, counts = np.unique(array, return_counts=True)

print('Unique Elements:', unique_elements)
print('Counts of Unique Elements:', counts)
