""" Fibonacci series: each number is the sum of the two preceding ones; start with 
    a = 0, b = 1, and use a while loop to print and update values (a, b = b, a+b) 
    until a reaches 10.
"""
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8

""" 
Multiple assignment (a, b = 0, 1) sets variables simultaneously, with right-hand 
expressions evaluated left-to-right before assignment; a while loop runs while 
a < 10 is true (non-zero or non-empty sequences are true, zero/empty are false), 
using comparison operators (<, >, ==, <=, >=, !=); the loop body uses indentation 
for grouping, requiring a blank line in interactive mode to signal completion.
"""