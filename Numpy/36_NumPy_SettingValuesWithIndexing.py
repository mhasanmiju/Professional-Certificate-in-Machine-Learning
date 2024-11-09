# xample 19: NumPy - Setting Values Using Indexing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Setting specific values using indexing
array[[0, 4]] = [99, 999]

print('Array after Setting Values:', array)
