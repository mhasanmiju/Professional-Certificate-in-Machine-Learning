import numpy as np

array1 = np.array([1, 3, 5])
array2 = np.array([2, 4, 6])

add = np.add(array1, array2)
subtract = np.subtract(array2, array1)
multiply = np.multiply(array1, array2)
divide = np.divide(array2, array1)

print(f"ADD: {add}\nSubtract: {subtract}\n")
print(f"Multiply: {multiply}\nDivide: {divide}\n")