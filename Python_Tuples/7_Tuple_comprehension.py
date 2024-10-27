# Tuples do not support comprehension like lists.
# However we can tke help from tuple creating function to create a tuple.

squared_tuple = tuple(x**2 for x in range(10))

print(f"Created tuple is: {squared_tuple}")
