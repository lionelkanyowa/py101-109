# Assignment: Mortgage Calculator:

# Welcoming user to the calculator
print("Welcome to the Mortgage Calculator")

# Asking user input for loan amount, APR and duration of loan.
print("Please enter the loan amount: ")
loan_amount = float(input())

print("What is the annual percentage rate? (APR): ")
annual_percentage_rate = float(input()) / 100

print("What is the duration of the loan in years? ")
loan_duration = float(input()) 

# Calculations for loan duration, interest rate, monthly payments and total payments.
loan_duration_months = loan_duration * 12
monthly_interest_rate = annual_percentage_rate / 12
monthly_payments = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
total_payments = monthly_payments * loan_duration_months
total_interest = total_payments - loan_amount 

# User output.
print(f"Your principal loan is {loan_amount}")
print(f"Your loan duration is: {loan_duration_months:.1f} months")
print(f"The total interest is amount: ${total_interest:.2f}")
print(f"You monthly payments will be ${monthly_payments:.2f} with a total payment of ${total_payments:.2f}")
