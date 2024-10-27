# The sort() method sorts a list in ascending order.
# We can also sort in descending order by setting the reverse parameter to True.

number_list = [5, 2, 9, 1, 5, 6]

#sorting in Ascending order

number_list.sort()
print(f"Ascending order list: {number_list}")

# Sorting in Descending order
number_list.sort(reverse=True)
print(f"Descending order list: {number_list}")