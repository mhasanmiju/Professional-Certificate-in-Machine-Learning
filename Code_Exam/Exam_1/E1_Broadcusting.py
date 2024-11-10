# Code_Exam/Exam_1/E1_Broadcusting.py
# a is a 3x1 array
# b is a 1x4 array
# Use broadcasting to perform an element-wise multiplication
# between a and b and print the resulting matrix.
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([[4, 5, 6, 7]])
resulting_matrix = a * b
print(f"Resulting Matrix: \n{resulting_matrix}")

