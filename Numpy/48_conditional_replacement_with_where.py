# 48_conditional_replacement_with_where.py

import numpy as np

# Creating an array
array = np.array([100, 15, 20, 27, 69])
# Replacing values based on condition
result = np.where(array > 25, 0, array)

print('Array with Values Greater Than 25 Replaced with 0:', result)
