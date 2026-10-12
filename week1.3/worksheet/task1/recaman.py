# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]  # Initialize the sequence with the first element
for n in range(1, L):
    prev = sequence[-1]
    next_num = prev - n
    if next_num > 0 and next_num not in sequence:
        sequence.append(next_num)
    else:
        sequence.append(prev + n)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence