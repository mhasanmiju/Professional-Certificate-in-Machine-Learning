#12_indexing_with_array.py
import numpy as np
array = np.array([[22,33,44],[55,66,77],[88,99,11]])
rows= np.array([0,1,2])
cols = np.array([0,1,2])
indexed_elements = array[rows, cols]

print(f"Indexed Elements: {indexed_elements}")