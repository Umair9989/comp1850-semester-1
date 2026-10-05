# Worksheet 1.2: Task 2 Solution
try:
    from util import read_numbers    
    numbers = read_numbers()   
    print(f"Maximum = {max(numbers)}")
    print(f"Minimum = {min(numbers)}")
    print(f"Mean = {sum(numbers) / len(numbers)}")
    num = ((len(numbers)) / 2)
    if num % 2 == 0:
        num1 = ((len(numbers) // 2) + ((len(numbers) // 2) + 1)) // 2
        print(f"Median = {numbers.sort[num1]}")
    elif num % 2 != 0:
        num2 = ((len(numbers) // 2) + 1) // 2
        print(f"Median = {numbers.sort[num2]}")
except:
    print("Error: no numbers provided")
    import sys
    sys.exit("Error")