# Creating a tuple using a generator expression for elements that meet a condition.

# Example range of numbers
numbers = range(11, 21)

# Creating a tuple of squares of even numbers
odd_squares = tuple(x**2 for x in numbers if x % 2 == 1)

print('Tuple of odd Squares:', odd_squares)
