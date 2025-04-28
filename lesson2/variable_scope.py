# PY100 exercises Variable Scope:

# 1.What will the following code do and why?
if True:
    my_value = 20

print(my_value)

# This code will output 20. Since the variable is assigned to a truthy value, within
# the if statement, then the output is 20. Also, with `if`, `for`, `while`, `match`, `with`, or `try` statements,
# Python does not adhere to any scoping rules like Ruby. So `my_value` is still accessible in the outer scope.

# 2.What will the following code do and why?
'''
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()
'''

# The code above will output an error. This is because in line 17 we are trying to reassign the local variable `x` before
# it is defined within the function. And even though `x` is defined in the outer scope, it still needs to be defined in the
# function. (UnboundLocalError)

# 3. What will the following code do and why?
'''
def my_function():
    a = 1

    if True:
        print(a)

my_function()
'''
# The code above will output 1. This is because the first scoping rule tells us that variables that are defined within a
# function are local to that function and cannot be accssed outside of that function, and since the function is being called on
# line 35, it can access the variable `a`, which is then evaluated within the if statement and printed to 1.

# 4. What will the following code do and why?
'''
a = 1

def my_function():
    print(a)

my_function()
'''
# The code above will print 1. This is because according to rule 3 of variable scope: Any variables that exist in the
# outer scope but not reassigned within the function, can be resused in that function. When the function call is executed
# on line 48, the print function is referencing to the global variable in line 1.

# 5.What will the following code do and why? Don't run it until you have tried to answer.
'''
a = 1

def my_functions():
    print(a)
    a = 2

my_functions()
'''
# The program above will output an error. When the the function call is executed in line 60, The function starts by executing
# The print statement to print a, but since a local variable exists on line 60, then `print(a)` will reference to that
# variable. In this case we are trying to print before the local variable has been defined, so print(a) has not reference to the
# variable `a`. Error: UnboundLocalError:

# 6.What will the following code do and why? Don't run it until you have tried to answer.
'''
a = 1

def my_function():
    a = 2

my_function()
print(a)
'''
# this code will output 1. In this example print(a) is pointing to the variable in the outer scope on line
# 71. Although we have a local variable within the function on line 74, the variable is not used, therefore when
# my_function() is called on line 76 nothing is outputed and it returns `None`.

# 7.What will the following code do and why? Don't run it until you have tried to answer.
''''
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)
'''
# The following code will output 2. Within the function, the global keyword is used on line 88, in this instance,  the `a`
# being modified is the variable `a` on line 85. Now `a` = 2 is accessible outside of the function. When `print(a)` is
# executed on line 92, the output will be 2.

# 8.What will the following code do and why? Don't run it until you have tried to answer.
'''
print(greeting)

greeting = 'Hello World'
'''
# The code above will print an `NameError`. Even though `greeting` is defined on line 98, `greeting` is being executed
# before the it's been defined. When print() looks for `greeting, it is unable to find it which will result in an error.
'''
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)
'''
# The code above will output 7. The print is referencing the variable `a` in the outer scope. Since integers are immutable, their
# values cannot be changed. In line 111, my_function passes through the variable `a` from the outer scope as an argument, which is then
# referenced by the local variable `b` within the function. In line 109 the operation taking place is b = b + 10(b = 7 + 10) which
# gives us 17 so now b is equal to 17. b is now referencing this new integer object meaning `a` is unaffected and retains its
# original value of 7 within the outerscope, hence `print(a)` is 7.

# 10.What will the following code do and why? Don't run it until you have tried to answer
b = [1, 2, 3]

def my_function():
   b[0] = 10

print(my_function())
print(b)
# The following code will output [1, 2, 3]. Although the variable `b` is modified within the function, it will return a
# `None`.
#
# Correct Answer:(Rule 3) The code will print: [10, 2, 3]. Since outer scope variables can be accessed from within the function,
# in line 124, instead of being reassigned, 'b' is still referencing the list object [1, 2, 3]. This is because there was no
# variable reassigment done within the function, so the `b` being modified in line 124 will mutate the `b` on line 121 and this is because
# lists are mutable.
