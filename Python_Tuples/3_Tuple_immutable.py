#Tuples are immutable so we can not change it's values.

my_tuple = (12,324,4566,676,86,'miju',[2,4],(12,2))

# Trying to modify an element (this will raise an error)
try:
    my_tuple[2] = 'Riju'
except TypeError as e:
    print('Error:', e)
