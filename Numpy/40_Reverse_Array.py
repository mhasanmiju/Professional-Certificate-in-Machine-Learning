# Numpy/40_Reverse_Array.py
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
reverse_array = array[:, : : -1 ]
print(f"Reverse array: {reverse_array}")