# We can iterate over a dictionary to access its keys, values, or key-value pairs.

my_dict = {"name": "Miju", "age": 26, "city": "Rangpur"}

for key in my_dict:
    print(f"Key: {key}")
    
for value in my_dict.values():
    print(f"Value: {value}")   
    
for key, value in my_dict.items():
    print(f"Key: {key} and value: {value}")