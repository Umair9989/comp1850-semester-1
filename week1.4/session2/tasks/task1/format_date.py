# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator="-"):
    # complete your code here

    formatted_date = f"{day}{separator}{month}{separator}{year}"
    return formatted_date
day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")
# Check if correct output is produced
print(format_data(day, month, year, "-"))
# Write code to test the function with separators such as "/", ":", "."
