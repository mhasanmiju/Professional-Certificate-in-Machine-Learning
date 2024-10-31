# Example 3: Set Comprehension with Condition

# Example list
numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Creating a set of odd numbers
odd_set = {num for num in numbers if num % 2 == 1}

print(f'Set of Odd Numbers: {odd_set}')