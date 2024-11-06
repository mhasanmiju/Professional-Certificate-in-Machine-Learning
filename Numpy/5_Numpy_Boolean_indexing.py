#5_Numpy_Boolean_indexing.py
import numpy as np
array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

boolean_index = array[array>25]
print(f'Elements Greater Than 25: {boolean_index}')