# Python can be used like a calculator.
# You can type expressions and get results.
# Use +, -, *, / for arithmetic and () for grouping.
print(2 + 2)
print(50 - 5*6)
print((50 - 5*6) / 4)
print(8 / 5) # division always returns a floating-point number


# Whole numbers like 2, 4, 20 are of type int.
# Numbers with decimals like 5.0, 1.6 are of type float.
# Using / always gives a float result.
# Use // for floor division (gets whole number result).
# Use % to get the remainder of a division.
print(17 / 3) # classic division returns a float
print(17 // 3)  # floor division discards the fractional part
print(17 % 3 ) # the % operator returns the remainder of the division
print(5 * 3 + 2) # floored quotient * divisor + remainder

#With Python, it is possible to use the ** operator to calculate powers [1]:
print(5 ** 2) # 5 squared   
print(2 ** 7) # 2 to the power of 7

# The = sign is used to assign a value to a variable.
# After assignment, Python doesn't show a result unless told to.
width = 20
height = 5 * 9
print(width * height)  # prints the result of the multiplication

#If a variable is not “defined” (assigned a value), trying to use it will give you an error:
  # try to access an undefined variable

# Python fully supports floating point numbers.
# If you use int and float together, the int is automatically converted to float.

print(4 * 3.75 - 1)  # multiplication with a float

# In interactive mode, the last printed result is stored in the variable _.
# This makes it easy to reuse the result for further calculations.

"""The variable _ that stores the last result only works in interactive mode, such as:
Python REPL (command line: python or python3)
Jupyter Notebook
IPython shell"""

tax = 12.5 / 100
price = 100.50
print(price * tax)  # calculate the tax on the price
price + _  # add the tax to the price
# The _ variable is not automatically printed, but you can print it if needed.
print(price + _)  # prints the total price including tax    
# Python has a built-in function called round() to round numbers.
# It can take two arguments: the number to round and the number of decimal places.
print(round(_, 2))  # rounds to two decimal places