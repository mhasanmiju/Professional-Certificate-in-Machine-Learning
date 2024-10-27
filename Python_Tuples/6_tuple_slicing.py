#Tuple slicing same as List
my_tuple = (12,324,4566,676,86,'miju',[2,4],(12,2))

#Slicing tuple from index 0 to 4
sliced_tuple = my_tuple[:4]
print(f'Sliced tuple from index 0 to 4: {sliced_tuple}')

#Slicing tuple from index 2 to 4
sliced_tuple2 = my_tuple[2:4]
print(f'Sliced tuple from index 2 to 4: {sliced_tuple2}')

#Slicing tuple from index 0 to end
sliced_tuple2 = my_tuple[0: :2]
print(f'Sliced tuple from index 0 to end but 2 steps: {sliced_tuple2}')