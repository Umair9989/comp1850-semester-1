import random

# Get user to input how many random numbers they want
numbers = input("How many random numbers do you want to generate: ")
count = int(numbers)

# Generate this many random numbers
random_numbers = [random.randint(1, 100) for _ in range(count)]

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as f:
    for num in random_numbers:
        f.write(str(num) + "\n")
