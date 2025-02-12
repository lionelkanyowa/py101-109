# 3. Build a program that asks the user tyo enter the length and width in a room, in meters, then prints the room's area in both 
# square meters and square feet.
#
# Note: 1 square meter == 10.7639 square feet.

width = float(input("Please enter the the width of the room: "))
length = float(input("Please enter the length of the room:"))

square_meter = length * width
square_feet = square_meter * 10.7639


print(f'\nYour area in square meter is: {square_meter:.2f} [m2].')
print(f'You area in square feet is: {square_feet:.2f} [ft2].')

# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it 
# and its conversion in parentheses.