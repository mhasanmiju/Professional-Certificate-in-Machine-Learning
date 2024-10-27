# List comprehension is a concise way to create lists using an expression and iteration.
# It can be used to generate new lists from existing ones.
# square of numbers from 0 to 4
squared_list = [x**2 for x in range(5)]

print(f"Squared list is: {squared_list}")

# Nested List Comprehension
Nested_List = [[x, y] for x in range(1, 4) for y in range(5, 7)]
print(f"Nested List is: {Nested_List}")

print(Nested_List[5][1])