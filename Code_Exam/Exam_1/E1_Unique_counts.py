# Create an array with 20 random integers between 1 and 15. Find and print:
# The unique elements in the array.
# The count of each unique element.
import numpy as np
array = np.random.randint(1, 16, size= 20)
unique_elements, counts = np.unique(array, return_counts= True)
print(f"Array: {array}")
print(f"Unique Element: {unique_elements}")
print(f"Unique Count: {counts}")