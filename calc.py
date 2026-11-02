pink = "\033[95m"
reset = "\033[0m"

num1 = float(input(f"{pink}Enter a number: {reset}"))
num2 = float(input(f"{pink}Enter a second number: {reset}"))

print(f"{pink}Enter 1 for +")
print("Enter 2 for -")
print("Enter 3 for *")
print(f"Enter 4 for /{reset}")
option = input(f"{pink}Enter your option: {reset}")

if option == "1":
    answer = num1 + num2
elif option == "2":
    answer = num1 - num2
elif option == "3":
    answer = num1 * num2
elif option == "4":
    if num2 == 0:
        print(f"{pink}Cannot divide by zero.{reset}")
        raise SystemExit
    answer = num1 / num2
else:
    print(f"{pink}Please choose 1, 2, 3, or 4.{reset}")
    raise SystemExit

print(f"{pink}Answer: {answer}{reset}")