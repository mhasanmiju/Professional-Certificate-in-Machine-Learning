# We can add elements to a set using the add() method.
# Sets do not allow duplicate elements.
#They do not support indexing, slicing, or other sequence-like behavior.
#The order of elements can vary each time you print or iterate over the set.

my_set = {1,3,5,7,9,2,4,6,8}
my_set.add(10)
# Trying to add a duplicate element (this will have no effect)
my_set.add(1)
print(f"Set is: {my_set}")