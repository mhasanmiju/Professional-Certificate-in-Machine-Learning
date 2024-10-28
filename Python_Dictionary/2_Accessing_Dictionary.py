# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless we use the get() method,
# which returns None.


my_dict = {"name": "Miju", "age": 26, "city": "Rangpur"}

name = my_dict["name"]
age = my_dict.get("age")
job = my_dict.get("job")

print(f"Name: {name} Age: {age} Job: {job}") 