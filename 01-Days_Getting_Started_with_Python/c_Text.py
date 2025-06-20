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

# Two or more string literals (enclosed in quotes) next to each other are 
# automatically concatenated.
print('Py' 'thon')
# Output: Hello World

# This feature is particularly useful when you want to break long strings.

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
#output: Put several strings within parentheses to have them joined together.

#This only works with two literals though, not with variables or expressions:

# String repetition and concatenation with * and + work only with literals, not 
# with variables or expressions, resulting in a SyntaxError if attempted.

prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
""" File "<stdin>", line 80
     prefix 'thon'
            ^^^^^^^
 SyntaxError: invalid syntax
""" 

('un' * 3) 'ium'  # expression with * and string literal
""" File "<stdin>", line 87
     ('un' * 3) 'ium'
                 ^^^^^
 SyntaxError: invalid syntax
"""


# Concatenate variables or a variable and a literal using +, index strings with 
# 0 as the first character (no separate character type), use negative indices 
# to count from the right (-1 is last), and slice substrings with [start:end].

prefix = 'Py'
print(prefix + 'thon')  # concatenate a variable and a literal
# Output: Python

word = 'Python'
print(word[0])  # character in position 0
# Output: P
print(word[5])  # character in position 5
# Output: n

print(word[-1])  # last character
# Output: n
print(word[-2])  # second-last character
# Output: o
print(word[-6])  # first character (same as 0)
# Output: P

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
# Output: Py
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
# Output: tho

# Slice indices default to 0 for the first index and the string length for the 
# second if omitted; start is included, end is excluded, ensuring s[:i] + s[i:] 
# equals s; examples include slicing from start to position 2, position 4 to end, 
# and second-last to end.

word = 'Python'
print(word[:2])  # characters from the beginning to position 2 (excluded)
# Output: Py
print(word[4:])  # characters from position 4 (included) to the end
# Output: on
print(word[-2:])  # characters from the second-last (included) to the end
# Output: on

# Demonstrate that s[:i] + s[i:] equals s
print(word[:2] + word[2:])
# Output: Python
print(word[4:] + word[:4])
# Output: Python

# Visualize string slices by imagining indices between characters (0 at the left 
# edge, n at the right of the last character); use negative indices for right-to-
# left counting; slice length is the difference of indices, and out-of-range 
# indices cause IndexError.

word = 'Python'
print(word[1:3])  # characters from position 1 to 3 (excluded), length is 2
# Output: yt
print(word[4:])   # characters from position 4 to end
# Output: on
print(word[-2:])  # characters from second-last to end
# Output: on

# Attempting an out-of-range index
print(word[42])  # the word only has 6 characters
# Output: Traceback (most recent call last):
#          File "<stdin>", line 154, in <module>
#          IndexError: string index out of range


# Out-of-range slice indices are handled gracefully, returning an empty string 
# if beyond the length; strings are immutable, so assigning to an index causes 
# TypeError; create a new string with concatenation instead.

word = 'Python'
print(word[4:42])  # characters from position 4 to 42 (out of range)
# Output: on
print(word[42:])   # characters from position 42 to end (out of range)
# Output: ''

# Attempting to assign to an index (immutable string)
word[0] = 'J'      # this will cause an error
# Output: Traceback (most recent call last):
#          File "<stdin>", line 1, in <module>
#          TypeError: 'str' object does not support item assignment

word[2:] = 'py'    # this will also cause an error
# Output: Traceback (most recent call last):
#          File "<stdin>", line 1, in <module>
#          TypeError: 'str' object does not support item assignment

# Create a new string instead
print('J' + word[1:])
# Output: Jython
print(word[:2] + 'py')
# Output: Pypy

# The built-in len() function returns the length of a string, counting all characters.

s = 'supercalifragilisticexpialidocious'
print(len(s))
# Output: 34