# cannot be removed an element directly we have to
# concatenating the existing one with another tuple.
my_tuple = (12,324,4566,676,86,'miju',[2,4],(12,2))

temp_list = list(my_tuple)
temp_list.remove(86)
my_tuple = tuple(temp_list)

print(f"Updated tuple: {my_tuple}")