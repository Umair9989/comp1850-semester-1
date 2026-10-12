# Task 3: Extra Practice - Grade Analyser

# ask for filename of the student file
filename = input("Enter the name of the student data file: ")

# open the file
file = open(filename, "r")

# read in the data, and for each student calculate their average grade and classification
scores = []
score = 0
input_file_name = filename.split(".")[0]
print(f"Processing file: {filename}")
feedback = open(input_file_name + "_out.csv", "w")

for line in file:
    # split the line into parts
    parts = line.strip().split(",")
    
    # the first part is the student ID
    student_id = parts[0]
    
    # the rest are module grades (may contain empty strings for unused modules)
    grades = []
    for part in parts[1:]:
        if part.strip() != "":
            grades.append(int(part))
    
    # calculate the average
    average = sum(grades) / len(grades)
    
    # determine classification
    if average >= 70:
        classification = "1"
    elif average >= 60:
        classification = "2:1"
    elif average >= 50:
        classification = "2:2"
    elif average >= 40:
        classification = "3"
    else:
        classification = "F"
    
    # write the result to the output file
    feedback.write(f"{student_id},{average:.2f},{classification}\n")

# close the files
file.close()
feedback.close()
