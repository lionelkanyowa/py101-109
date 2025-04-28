# Truthiness Exercises: Lesson 2 chapter
#
# 1. To what values do the following expressions evaluate?
print(False or (True and False)) # False
print(True or (1 + 2))           # True
print((1 + 2) or True)           # 3
print(True and (1 + 2))          # 3
print(False and (1 + 2))         # False
print((1 + 2) and True)          # True
print((32 * 4) >= 129)           # False
print(False != (not True))       # False
print(True == 4)                 # False
print(False == (847 == '847'))   # True
print()

# 2. Write a function, even_or_odd, that determines whether its argument is an even or odd
# number. If it's even, the function should print 'even'; otherwise, it should print 'odd'.
# Assume the argument is always an integer.

def even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'

print(even_or_odd(4))
print(even_or_odd(11))
print(even_or_odd(102))
print(even_or_odd(44))
print()

# 3.Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)
# Line 41 outputs Product2 since the case matches the string `113` on line 34.
# Line 42 outputs Product not found! since there's no cases with string srguments that matches the numeric value 142.
# There for it matches with the "default' case `_`.

# 4.Refactor the statement to use a regular `if` statement instead.
# return ('bar' if foo() else qux())

# if foo():
    # return bar
# else:
    # return qux()

# 5. What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
# This code will output 'Empty'. When calling the function on line 62, we are passing through an empty list as an argument.
# Since almost all objects in Python in are truthy except for a select few, an empty list is one of those few objects that
# is considered as falsy. When the empty list is evaluated in the `if/else` statement, it skips the `if` statement that only accepts
# truthy values and is evaluated by the else statement which then evaluates it as falsy and hence we get the output of 'Empty'
#
# 6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer
# than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD',
# but don't change 'goodbye'.

def all_caps(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(all_caps('This is a way to test truthiness.'))
print(all_caps('Lionel'))
print(all_caps('originally, this was all in lowercase!'))
print(all_caps('Hello, world!'))
print(all_caps('all lower'))

# Write a function that takes a single integer argument and prints a message that describes whether:
# - the value is 0 and 50 inclusive
# - the value is 51 and 100 inclusive
# - the value is greater than 100
# - the value is less than 100

def number_range(num):
    if num < 0:
        print(f'{num} is less than 0')
    elif num <= 50:
        print(f'{num} is between 0 and 50')
    elif num <= 100:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is greater than 100')

number_range(22)
number_range(-3)
number_range(122)
number_range(74)
number_range(100)
number_range(51)
