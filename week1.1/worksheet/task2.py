"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohammed Umair Ahmed
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

while True:
    print("Please enter the amount that you would like to save monthly, this must be an integer (a whole number)")
    monthly = input()
    try:
        monthly_Saving = int(monthly)
        break
    except ValueError:
        print(f"{name}, the value you entered is not an integer amount")

print(f"You are going to save £{monthly_Saving} monthly")
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
year_saving = monthly_Saving * 12
print(f"You are going to save £{year_saving} yearly")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = year_saving * 0.8
print(f"the amount of interest on your total savings will be £{interest:.2f}")
total_saving = year_saving + interest
print(f"In total you will save £{total_saving:.2f}")
