# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
f = open("glasses.txt")
print(f.read())
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
count = 0
with open('glasses.txt', 'r') as f:
    data = f.read()
    words = data.split()
    count += len(words)

# display the wordcount
print("Total Words:" ,count)
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210