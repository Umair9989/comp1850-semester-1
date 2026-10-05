# Worksheet 1.2: Task 1 Solution
import sys

try:
    score_input = input("Enter a grade in the range 0 to 100: ")
    score = int(score_input)
    
    if 0 <= score <= 39:
        print(f"{score} is a Fail")
    elif 40 <= score <= 69:
        print(f"{score} is a Pass")
    elif 70 <= score <= 100:
        print(f"{score} is a Distinction")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")

except (ValueError, EOFError, KeyboardInterrupt):
    sys.exit("Error: Grade must be an integer between 0 and 100")
