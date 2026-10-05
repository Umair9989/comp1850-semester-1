# Worksheet 1.2: Task 1 Solution
score = (input("Enter a grade in the range 0 to 100: "))
try: 
    if int(score) >= 0 and int(score) <= 39:
        print(f"{score} is a Fail")
    elif int(score) >= 40 and int(score) <= 69:
        print(f"{score} is a Pass")
    elif int(score) >=70 and int(score) <= 100:
        print(f"{score} is a Distinction")   
    else:
        print("Error: Grade must be an integer between 0 and 100")
        import sys
        sys.exit("Error!")
except:
    print("Error: Grade must be an integer between 0 and 100")
    import sys
    sys.exit("Error!")
