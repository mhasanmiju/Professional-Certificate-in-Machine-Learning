# 39_Upper_triangle.py
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
upper_triangle = np.triu(array)
print(f"Upper Triangle: \n{upper_triangle}")