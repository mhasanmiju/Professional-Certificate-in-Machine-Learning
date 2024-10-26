# We can remove an elements by using remove() and pop()
# remove() deletes the first occurrence of the given value and pop() deletes by giving index.
 
my_list = ['a','b','c','d']
print(f"Before removing the list:{my_list}")

# Removing elements
my_list.remove('b')
print(f"After remove b:{my_list}")

poped_item = my_list.pop(2)
print(f"After poped index 2:{my_list}") 