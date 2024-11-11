# Python_List/11_listcomprehension_lambdafunction.py
# Squaring Only Even Numbers
numbers = [1, 2, 3, 4, 5, 6]

# Using a lambda function with a list comprehension
squared_evens = [(lambda x: x**2 if x % 2 == 0 else x)(n) for n in numbers]

print(squared_evens)
