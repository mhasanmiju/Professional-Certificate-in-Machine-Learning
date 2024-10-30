# Example nested list
nested_list = [[1, "Miju", 3], [11, 10, [5, 6,8]], ["ML", 9]]


# Accessing a nested element
nested_element = nested_list[1][2][2]
print(f"Accessed Element is: {nested_element}")

# Modifying a nested element
nested_list[2][0] = "Ai"
print(f"Modified Element is: {nested_list}")

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten and extend
        else:
            flat_list.append(item)  # Append non-list item directly
    return flat_list


flattened_list = flatten(nested_list)
print(f"Flattened list: {flattened_list}") 
