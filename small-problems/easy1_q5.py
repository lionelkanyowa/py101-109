# 4.Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, 
# then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

bill = float(input('What is the bill?:'))
print(f'You entered ${bill}\n')

percentage_value = float(input('What is the tip percentage?:'))
print(f'Tou entered {percentage_value}%\n')

tip = (percentage_value / 100) * bill
total_bill = percentage_value + bill

print(f'The tip is: ${tip:.2f}')
print(f'The total is ${total_bill:.2f}')



