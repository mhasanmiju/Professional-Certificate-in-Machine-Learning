# Elements in either set, but not in both.

A = {1,3,5,7,9,11,12}
B = {2,4,6,8,10,11,12}
# We can perform Symmetric difference in two ways
symmetric_difference1 = A ^ B
symmetric_difference2 = A.symmetric_difference(B)

print(f"1st way of symmetric difference: {symmetric_difference1}")
print(f"2nd way of symmetric difference: {symmetric_difference2}")