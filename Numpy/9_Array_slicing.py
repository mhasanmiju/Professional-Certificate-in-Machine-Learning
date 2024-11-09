#9_Array_slicing.py
import numpy as np

array = np.array([range(11, 22, 2)])
print(f"Array: {array}") #out: Array: [[11 13 15 17 19 21]]

sliced_array = array[0, 1: 4: 2] # only a row in this array that is why 0 
                                 # and column will 
                                 # print 2 step 13, 17 and 19 won't print out of rage it 4

print(f"Sliced array: {sliced_array}")
