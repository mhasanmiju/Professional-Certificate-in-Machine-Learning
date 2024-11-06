import numpy as np

# Array of indices
array = np.array([0, 1, 2, 0])

# Choices: List of arrays
choices = [array * 2, array + 10, array ** 2]
print(f'Choice Array: {choices}')

'''
choices = [[0, 2, 4, 0],       # Result of array * 2
           [10, 11, 12, 10],   # Result of array + 10
           [0, 1, 4, 0]]       # Result of array ** 2 
'''
# Using np.choose to apply different conditions
result = np.choose(array, choices)

print(f'Result using np.choose: {result}')

#array[0] is 0
# Index	array Value	choices[array[i]] (Selected Element)
#   0	         0	choices[0][0]      → 0
#   1	         1	choices[1][1]      → 11
#   2	         2	choices[2][2]      → 4
#   3	         0	choices[0][3]      → 0