
# 25_NumPy_StatisticalFunctions.py
import numpy as np

# Creating an array
array = np.array([10, 20, 50, 60, 70])

# Calculating statistical values
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)
variance = np.var(array)

print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
print('Variance:', variance)
