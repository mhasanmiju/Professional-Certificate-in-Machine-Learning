# Performing union, intersection, and symmetric difference with three sets.
# sets
set1 = {1, 2, 3, 4, 9}
set2 = {3, 4, 5, 6, 9}
set3 = {5, 6, 7, 8, 9}

# Union: All unique elements from all three sets
union_result = set1 | set2 | set3
#or
union_result = set1.union(set2, set3)
print("Union:", union_result)

# Intersection: Elements that are common to all three sets
intersection_result = set1 & set2 & set3  
# or
intersection_result = set1.intersection(set2, set3)
print("Intersection:", intersection_result)

# Symmetric Difference: Elements that are in any of the sets but not in all three
symmetric_difference_result = (set1 ^ set2 ^ set3)  
# or
symmetric_difference_result = set1.symmetric_difference(set2).symmetric_difference(set3)

#using the symmetric difference across three sets doesn’t 
# exclude elements present in all three sets.
# Subtracting common_in_all(Find the intersection) from symmetric_difference_result 
# excludes elements that appear in all three sets.

symmetric_difference_result = symmetric_difference_result - intersection_result 
print("Symmetric Difference:", symmetric_difference_result)