# 1
# True False

# 2
# and or not

# 3
# True and False = False
# False and True = False
# True and True = True
# False and False = False
#
# True or True = True
# False or False = False
# True or False = True
# False or True = True
#
# not True = False
# not False = True

# 4
False
False
True
False
False
True

# 5
# >, <, >=, <=, ==, !=

# 6
# == is used to compare two values and returns a boolean value
# = is used to assign a value to a variable

# 7
# A condition is a statement that can be evaluated as True or False and is used to control the flow of a program

# 8
# The three blocks of code are the if block, the else block, and the others block

# 9
spam = input()

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


# 10
# Press Ctrl+C to stop the program.

# 11
# The break statement is used to exit a loop
# The continue statement is used to skip the current iteration of a loop and continue with the next iteration

# 12
# range(10) will return a range object that represents the numbers 0 to 9
# range(0, 10) will return a range object that represents the numbers 0 to 9 explicitly tell the loop to start at 0
# range(0, 10, 1) will return a range object that represents the numbers 0 to 9 and explicitly tell the loop to start at 0 and increment by 1

# 13
for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i = i + 1

# 14
# Type 1.
import spam
spam.bacon()

# Type 2.
from spam import bacon
bacon()