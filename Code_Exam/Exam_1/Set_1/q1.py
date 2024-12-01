"""
Write a Python script that prompts the user to enter a list of integers 
separated by spaces.
a) Print all the even numbers in the list.
b) Calculate and print the sum of all odd numbers in the list.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

number = input("Enter the integer list separated by spaces: ")
int_list = list(map(int, number.split()))
#or
int_list2 = [ int(num) for num in number.split()]

even = [num for num in int_list if num % 2 == 0]
odd = [num for num in int_list if num % 2 == 1]
odd_sum = sum(odd)

print(f"Even numbers: {even}")
print(f"odd numbers: {odd}\nSum of odds:{odd_sum}")