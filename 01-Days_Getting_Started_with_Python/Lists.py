"""
    Lists are versatile compound data types using square brackets [], typically 
    holding items of the same type; they support indexing, slicing, concatenation 
    with +, and are mutable, allowing content changes unlike immutable strings.
"""
squares = [1, 4, 9, 16, 25]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Indexing and slicing
print(squares[0])  # indexing returns the item
# Output: 1
print(squares[-1])  # last item
# Output: 25
print(squares[3:])  # slicing returns a new list
# Output: [16, 25]

# Concatenation
print(squares + [36, 49, 64, 81, 100])
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Mutability
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
# Output: 64
cubes[3] = 64  # replace the wrong value
print(cubes)
# Output: [1, 8, 27, 64, 125]

# Add items to a list end with append(), note that list assignment references 
# the same object (changes reflect across variables), and slice operations 
# return a new shallow copy of the list.

cubes = [1, 8, 27, 64, 125]
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
# Output: [1, 8, 27, 64, 125, 216, 343]

# List assignment references the same object
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object
# Output: True
rgba.append("Alph")
print(rgb)
# Output: ['Red', 'Green', 'Blue', 'Alph']

# Slice operations return a new list (shallow copy)
correct_rgba = rgb[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
# Output: ['Red', 'Green', 'Blue', 'Alpha']
print(rgba)
# Output: ['Red', 'Green', 'Blue', 'Alph']

# Assignment to slices can change list size or clear it entirely; use len() to 
# get list length; lists can be nested, containing other lists for complex structures.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# Output: ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# Now remove them
letters[2:5] = []
print(letters)
# Output: ['a', 'b', 'f', 'g']

# Clear the list by replacing all elements with an empty list
letters[:] = []
print(letters)
# Output: []

# The built-in function len() also applies to lists
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# Output: 4

# Nesting lists (lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# Output: [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])      # Output: ['a', 'b', 'c']
print(x[0][1])   # Output: 'b'