# Slicing allow to extract a part of list
#It is done using a colon (:) to specify start, stop, step indices.

my_list = [10,20,30,40,50]
print(f'List before sliced: {my_list}')
#Slicing list from index 1 to 4
sliced_list = my_list[1:4]
print(f'Sliced list from index 1 to 4: {sliced_list}')

#Slicing list from index 2 to 4
sliced_list2 = my_list[2:4]
print(f'Sliced list from index 2 to 4: {sliced_list2}')

#Slicing list from index 0 to 5
sliced_list2 = my_list[0:5:2]
print(f'Sliced list from index 0 to 4 but 2 steps: {sliced_list2}')