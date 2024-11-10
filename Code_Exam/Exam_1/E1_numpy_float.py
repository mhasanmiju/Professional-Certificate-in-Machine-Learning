# Create a 5x5 matrix with random float between 1 and 100. Find and print:
# The sum of all elements.
# The mean of the elements in the matrix.
# The maximum and minimum values in the matrix.

import numpy as np

# Create a 5x5 matrix with random float values between 1 and 100
matrix = np.random.uniform(1, 100, size=(5, 5))

# Calculate the sum of all elements
matrix_sum = np.sum(matrix)

# Calculate the mean of the elements in the matrix
matrix_mean = np.mean(matrix)

# Find the maximum and minimum values in the matrix
matrix_max = np.max(matrix)
matrix_min = np.min(matrix)

# Print results
print("Matrix:")
print(matrix)
print("\nSum of all elements:", matrix_sum)
print("Mean of the elements:", matrix_mean)
print("Maximum value:", matrix_max)
print("Minimum value:", matrix_min)
