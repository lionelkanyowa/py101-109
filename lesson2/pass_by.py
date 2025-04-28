# Pass by value vs pass by reference

# def change_name(name):
    # print(name)


# name = 'jim'
# change_name(name)
# print(name)
'''
num = 5
def my_func():
    print(num)

my_func()
'''

def exclaim(lst):
    for sentence in lst:
        # print(lst)
        sentence.capitalize()
        print(lst)
        sentence += '!'

        # print(lst) # what will this output? # ['twist it', 'spin it', 'bop it']

actions = ['twist it', 'spin it', 'bop it']
exclaim(actions)
