# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum 
# or the product of all numbers between 1 and the entered integer, inclusive.
#====================================================================================
# Example 1:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s
# 
# The sum of the integers between 1 and 5 is 15.
# ===================================================================================
# Example 2: 
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.
#=====================================================================================

number = int(input('Please enter an integer greater than 0: '))
print(f'You entered {number}\n')

choice = input("""Enter "s" to compute the sum, or "p" to compute the product: """)



def sum_or_product(number, choice):
    if number > 0:
        return number
    else:
        print('Number must be more than 0')
    
    total_sum = 1
    for num in range(number):
        total_sum += num
    return total_sum

    total_product = 1
    for num in range(number):
        total_product += num
    return total_product






