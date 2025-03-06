# q.4 Use the multiply function from the "multiplying Two Numbers" exercise, wite a function that computes the square of its
# argument (the square is the result of multiplying a number by itself). 

def multiply(x, y):
    return x * y

def square_number(num):
    return multiply(num, num)

print(square_number(5) == 25)
print(square_number(-8) == 64)