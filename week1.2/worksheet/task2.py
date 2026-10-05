import sys
from util import read_numbers

try:
    numbers = read_numbers()
    
    if not numbers:
        raise ValueError
        
    print(f"Maximum = {max(numbers)}")
    print(f"Minimum = {min(numbers)}")
    print(f"Mean = {sum(numbers) / len(numbers)}")
    
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[(n // 2) - 1] + numbers[n // 2]) / 2
        if isinstance(median, float) and median.is_integer():
            median = int(median)
            
    print(f"Median = {median}")

except (ValueError, ZeroDivisionError, EOFError, KeyboardInterrupt):
    sys.exit("Error: no numbers provided")
