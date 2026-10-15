# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ["dog", "cat", "hamster", "goldfish"]

# Original list comprehension
not_fish = [item for item in animals if item != "goldfish"]
print("List comprehension result:", not_fish)


# Equivalent for loop
not_fish_loop = []
for item in animals:
    if item != "goldfish":
        not_fish_loop.append(item)

# Print your result to verify it is the same
print("For loop result:        ", not_fish_loop)
