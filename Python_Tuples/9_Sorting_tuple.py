# We can not sor a tuple directly byt  We can use the sorted() function,
# which works directly on tuples and returns a sorted list.
# we can then convert it back to a tuple.

my_tuple = (2,1,4,67,8,7,99,00,9,8,6)
sorted_list=sorted(my_tuple)
sorted_tuple = tuple(sorted_list)
print(f"Sorted tuple is: {sorted_tuple}")