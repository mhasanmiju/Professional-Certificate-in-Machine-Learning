#13_Reshaping_array.py
import numpy as np

array = np.arange(9)

#creating 3x3 array
reshaped_array= array.reshape(3,3)

print(f"new array: {reshaped_array}")
print(f"Dimension of the array: {reshaped_array.ndim}")
