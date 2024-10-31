# Using list comprehension with nested loops and conditions to filter elements.

# Example matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flattening and filtering odd numbers from the matrix
even_flattened = [num for row in matrix for num in row if num % 2 == 1]

print('Flattened odd Numbers:', even_flattened)