# 45_mask_index.py
import numpy as np
array = np.array([[1, -5, 2],[4,5,-6]])
# Positive values are masked
masked = np.ma.masked_where(array>0, array)
 
print(f"Masked index: {masked}")