import numpy as np

# Creating arrays with different functions
array_zeros = np.zeros((2, 3))
array_ones = np.ones((3, 3))
array_full = np.full((2, 2), 7)
array_range = np.arange(9)
nd_range = array_range.reshape(3,3)
print(f'Array of Zeros: \n{array_zeros}')
print(f'Array of ones: \n{array_ones}')
print(f'Array with All Elements as 7: \n{array_full}')
print(f'Array with Range of Numbers: \n{array_range}')
print(f'Array with Range 2D: \n{nd_range}')
