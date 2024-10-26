# We can add elements to a list by using append() or insert() method
# append() adds an element to the end and insert() adds an element to a specific index.

my_list = [1,2,3]

#adding an element
my_list.append(4)
my_list.insert(1,'Inserted')

#printing updated list
print(f"Updated list: {my_list}")