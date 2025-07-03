# In python there mainly two types of numbers: integers(int) and floating-point numbers (float).
# Integers are the whole number without decimal points, while floating-point numbers are the numbers with decimal points.
# the above are the basic types of numbers in python, but there are other types of numbers like complex numbers that have a real and imaginary part.

# in this code we try to cover the basic operations that operate on numbers such as addition, subtraction, multiplication, division, exponentiation, and other.

# General rules in arithemetic operations: between integer and integer give interger result otherwise give float result.

num1 = 10
num2 = 5
# Addition
sum = num1 + num2
# Substraction 
difference = num1 - num2
# Multiplication
product = num1 * num2
# Division
quotient = num1 / num2
# Floor Division 
floor_quotient = num1 // num2
# Exponentiation 
exponent = num1 ** 2
# Modulus (Remainder form division)
remainder = num1 % 3
# Absolute value
x = -10
absolute_value = abs(-x)
# Round a number 
rounded_value = round(3.5654545,3) # Round to 3 decimal places
# Maximun and Minimum 
maximum_value = max(num1, num2)
minimum_value = min(num1, num2, 0) # 0 is the third argument

# print the results
print(sum) # Output: 15
print(difference) # Output: 5
print(product) # Output: 50
print(quotient) # Output: 2.0
print(floor_quotient) # Output: 2
print(exponent) # Output: 100
print(remainder) # Output: 1
print(absolute_value) # Output: 10
print(rounded_value) # Output: 3.565
print(maximum_value) # Output: 10
print(minimum_value) # Output: 0
# Note in python 3 the division operator (/) always returns a float result, even if both are integers.
# In python 2, the division operator (/) returns an interger if both operands are integers.
# In python 3, you can get an integer when dividing two numbers by using the floor division operator (//).
