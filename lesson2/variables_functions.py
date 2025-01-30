my_var = [1]

def my_func(my_var):
    my_var = [2]

my_func(my_var)
print(my_var)

my_var1 = 'Hello'

def my_func():
    return my_var1 + ' world'

print(my_func())
print(my_var1)