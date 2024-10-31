# Goal for Unpacking a tuple is insert multiple values into  variables, 
# using the * operator for remaining values.

# Example tuple
person_info = ('Miju', 26, 'Dhaka', 'Engineer', 'Single', 'Travel', 'Sports')

# Unpacking tuple into variables
name, age, *other_details = person_info
other_details, hobbies = other_details[:3], other_details[3:]
print(f'Name: {name}\nAge: {age}\nOther Details:{other_details}\nHobbies: {hobbies}')
