# Elements in the first set but not in the second.

A = {1,3,5,7,9,11,12}
B = {2,4,6,8,10,11,12}
# We can perform set difference in two ways
set_difference1 = A - B
set_difference2 = A.difference(B)

print(f"1st way of Set difference: {set_difference1}")
print(f"2nd way of Set difference: {set_difference2}")