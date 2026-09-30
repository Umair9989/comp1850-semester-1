# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #Prints the string the user entered
print(f"Modified String 1: {user_string.lower()}") #Prints the string in all lower case
print(f"Modified String 2: {user_string.upper()}") #Prints the string in all uppercase
print(f"Modified String 3: {user_string.strip()}") #Removes all whitespace before and after the string
print(f"Modified String 4: {user_string.replace('a', '@')}") #Prints the string replacing all of the 'a' characters with the '@' symbol
print(f"Modified String 5: {user_string.capitalize()}") #Prints the string with only a capital letter on the first character
print(f"Modified String 6: {user_string[::-1]}") #Prints the string in reverse order
print(f"Modified String 7: {user_string.title()}")  #Prints the string capatilising each word in the string
print(f"Modified String 8: {len(user_string)}") #Prints the length of the string the user entered
print(f"Modified String 9: {user_string.find('a')}") #Prints the position of the character 'a'
print(f"Modified String 10: {user_string.count('a')}") #Counts how many 'a's' are present in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") #Checks to see if the string starts with 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}") #Checks to see if the string ends with '!'
print(f"Modified String 13: {user_string.isalnum()}") #Checks to see if the string is alphanumeric
print(f"Modified String 14: {user_string.isalpha()}") #Checks to see if the string only contains letters
print(f"Modified String 15: {user_string.isdigit()}") #Checks to see if the string only contains digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!