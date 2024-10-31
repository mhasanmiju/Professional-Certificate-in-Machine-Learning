# Converting a list of tuples into a dictionary using a loop.

# Initial list of tuples
tuple_list = [('a', 1, 3), ('b', 2, 5), ('c', 3, 7), ('d', 4, 9)]

# Convert to dictionary
result_dict = {key: [value1, value2] for key, value1, value2 in tuple_list}

# Display the result
print(result_dict)
