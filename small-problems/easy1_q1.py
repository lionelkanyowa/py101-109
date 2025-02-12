# Write a function that takes one integer argument and returns `True` when the number's absolute value is odd,
# False otherwise.

def is_odd(num):
    return(True if int(num) % 2 != 0 else False)
        # return True
    # else:
        # return False
# def is_odd(num):
    # return abs(num) % 2 == 1
    
print(is_odd(5))
print(is_odd(6))
print(is_odd(35))
print(is_odd(112))
print(is_odd(23))
print(is_odd(0))
