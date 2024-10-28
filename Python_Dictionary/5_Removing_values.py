# You can remove key-value pairs using the pop() method, 
# which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or 
# clear() to remove all items.

my_dict = {"name": "Miju", "age": 26, "city": "Rangpur"}

my_dict.pop("city")

print(f"Updated dictionary: {my_dict}")
