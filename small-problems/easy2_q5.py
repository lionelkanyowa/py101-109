# q.5 Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on 
# those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

def prompt(message):
    print(f"==> {message}")

prompt("Enter the first number: ")
num1 = float(input())

prompt("Enter the second number: ")
num2 = float(input())

prompt(f"{num1} + {num2} = {num1 + num2}")
prompt(f"{num1} - {num2} = {num1 - num2}")
prompt(f"{num1} * {num2} = {num1 * num2}")
prompt(f"{num1} / {num2} = {num1 / num2}")
prompt(f"{num1} // {num2} = {num1 // num2}")
prompt(f"{num1} % {num2} = {num1 % num2}")
prompt(f"{num1} ** {num2} = {num1 ** num2}")