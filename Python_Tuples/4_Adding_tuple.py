# Tuples are immutable that is why we can not add a value directly
# But we can create a new tuple by concatenating the existing one with another tuple.
my_tuple = (12,324,4566,676,86,'miju',[2,4],(12,2))

# Adding elements by creating a new tuple
my_tuple = my_tuple + ('Hi',)

print(f"Updated tuple is: {my_tuple}")
