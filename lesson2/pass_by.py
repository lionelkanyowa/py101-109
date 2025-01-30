# Pass by value vs pass by reference

def change_name(name):
    name = 'bob'

name = 'jim'
change_name(name)
print(name)

def add_element(my_list):
    my_list + [4]

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)