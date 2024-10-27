# We can check a value present or not in the tuple using "in" keyword.
my_tuple = (12,324,4566,676,86,'miju',[2,4],(12,2))

if 'Miju'.lower() in my_tuple:
    print(f"Miju is present in Tuple")
else:
    print(f"Miju is not present in Tuple")