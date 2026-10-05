# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Kwando"] = "Angola"
rivers["Mono"] = "Benin"
# Display all the keys
for x in rivers.keys():
    print(x)
# Display all the values
for y in rivers.values():
    print(y)
# Display all the key:value pairs, as tuples
print(list({"London": "Thames", "Leeds": "Aire", "Liverpool": "Mersey", "Kwando": "Angola", "Mono": "Benin"}.items()))
# Delete an entry from the rivers database
rivers.pop("London")
print(rivers)