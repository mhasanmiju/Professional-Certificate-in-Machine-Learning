#from this matrix Extract a 2x2 sub-matrix from the bottom right corner and print it.
import numpy as np
array = np.array([[5,10,15,20], [25,30,35,40],[45,50,55,60], [65,70,75,80]])
sub_matrix = array[2: , 2: ]

print(f"Sub_matrix: {sub_matrix}")