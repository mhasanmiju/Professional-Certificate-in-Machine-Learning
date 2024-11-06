#Exponential Functions
import numpy as np

x = np.array([1, 2, 3])
result = np.exp(x)
print("Exponential (e^x):", result)

# np.power(array, power)
array_power = np.power(x, 3)
print("Exponential (x^3):", array_power)
# np.power(power, array)
power_array = np.power(3, x)
print("Exponential (3^x):", power_array)

# np.log(x)
result = np.log(x)
print("Natural Logarithm (ln(x)):", result)


# Summary Table of Exponential and Logarithmic Functions in NumPy
#
# | Function         | Description                        |
# |------------------|------------------------------------|
# | np.exp(x)        | e^x                               |
# | np.exp2(x)       | 2^x                               |
# | np.power(a, x)   | a^x                               |
# | np.log(x)        | Natural log (base e)              |
# | np.log10(x)      | Log base 10                       |
# | np.log2(x)       | Log base 2                        |
# | np.log1p(x)      | ln(1 + x)                         |
# | np.expm1(x)      | e^x - 1                           |
