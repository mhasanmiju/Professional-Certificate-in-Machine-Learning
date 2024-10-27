# We can add elements to a list by using append() or insert() method
my_list = [1,2,3]

# append() adds an element to the end.
my_list.append(4)

# Extend list with multiple elements
my_list.extend([7, 8])
print(f"1st Updated list: {my_list}")
# insert() adds an element to a specific index.
my_list.insert(1,'Inserted')
print(f"2nd Updated list: {my_list}")
my_list.insert(2, 2.5)

#printing updated list
print(f"Updated list: {my_list}")