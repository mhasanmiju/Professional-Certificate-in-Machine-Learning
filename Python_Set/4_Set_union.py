# union() method returns a new set containing all unique elements from both sets.

A = {1,3,5,7,9}
B = {2,4,6,8,10}
# We can perform set union in two ways
set_union1 = A | B
set_union2 = A.union(B)

print(f"1st way of Set Union: {set_union1}")
print(f"2nd way of Set Union: {set_union2}")