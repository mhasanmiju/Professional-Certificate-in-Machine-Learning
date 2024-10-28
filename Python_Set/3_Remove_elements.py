# remove elements using the remove() or discard() methods.
# remove() method raises an error if the element is not found, while discard() does not.

my_set = {1, 4, 3.14, "Hello", (5, 6)}
my_set.remove(3.14)
my_set.discard(5)
print(f"Updated set: {my_set}")