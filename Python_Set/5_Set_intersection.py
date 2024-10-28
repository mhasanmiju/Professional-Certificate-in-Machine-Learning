# The intersection() method returns a new set containing common elements from both sets.

A = {1,3,5,7,9,11,12}
B = {2,4,6,8,10,11,12}
# We can perform set intersection in two ways
set_intersection1 = A & B
set_intersection2 = A.intersection(B)

print(f"1st way of Set intersection: {set_intersection1}")
print(f"2nd way of Set intersection: {set_intersection2}")