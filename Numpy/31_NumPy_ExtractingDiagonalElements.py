# Numpy/31_NumPy_ExtractingDiagonalElements.py
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the main diagonal
diagonal_elements = np.diag(matrix)

print(f'Matrix Elements:\n{matrix}')
print(f'Diagonal Elements:\n{diagonal_elements}')
