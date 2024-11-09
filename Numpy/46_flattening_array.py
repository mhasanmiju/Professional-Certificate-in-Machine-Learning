# 46_flattening_array.py
import numpy as np
array = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])
flattening_array = array.flatten() 
print(f"Flattened array: {flattening_array}")