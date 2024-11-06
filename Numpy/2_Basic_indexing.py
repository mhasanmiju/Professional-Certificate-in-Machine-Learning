import numpy as np

# Creating an array
array = np.array([22, 25, 35, 60, 30])

# Accessing elements by index
first_element = array[0]
last_element = array[-1]

# Slicing the array
slice_array = array[1:4]

print(f"First Element: {first_element}\nSecond Element: {last_element}")
print(f"Sliced Array: {slice_array}")