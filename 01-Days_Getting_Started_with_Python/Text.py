# Python handles text as strings (str type), including characters ("!"), words ("rabbit"), 
# names ("Paris"), sentences ("Got your back."), and more ("Yay! :)"). Strings can be 
# enclosed in single ('') or double ("") quotes interchangeably.

print('spam eggs')  # single quotes
print("Paris rabbit got your back :)! Yay!")  # double quotes
print('1975')  # digits and numerals enclosed in quotes are also strings

# To include a quote within a string, escape it with \ or use the other quotation mark type.

print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

# In the Python shell, the string definition and output string can look different. 
# The print() function produces a more readable output, by omitting the enclosing 
# quotes and by printing escaped and special characters:

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
'First line.\nSecond line.'

print(s)  # with print(), special characters are interpreted, so \n produces new line
# Output will be:
# First line.
# Second line.

# To prevent \ from being interpreted as special characters, use raw strings by 
# adding r before the first quote. Without r, \n creates a newline; with r, \n 
# is treated as literal text.

print('C:\some\nname')  # here \n means newline!
# Output: C:\some
#         name

print(r'C:\some\nname')  # note the r before the quote
# Output: C:\some\nname

# String literals can span multiple lines using triple-quotes (""" or '''). 
# End-of-line characters are included, but can be prevented by adding \ at line 
# end. Initial newline is excluded with \. 

print("""\
Usage: thingy [OPTIONS]
     -h                Display this usage message
     -H hostname       Hostname to connect to
""")
# Output:
# Usage: thingy [OPTIONS]
#      -h                Display this usage message
#      -H hostname       Hostname to connect to


#Strings can be concatenated with + or repeated with *.
# 3 times 'un', followed by 'ium'

print(3 * 'un' + 'ium')
# Output: unununium