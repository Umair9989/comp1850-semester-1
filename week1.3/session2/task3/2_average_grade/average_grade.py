# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
# Open and read all lines into a list
with open('student_data.csv', mode='r', encoding='utf-8') as infile:
    # Read lines and strip newline characters
    data = [line.strip().split(',') for line in infile.readlines()]

# Create a fresh report file
with open('report.txt', mode='w', encoding='utf-8') as outfile:
    # Skip the header row using slicing data[1:]
    for row in data[1:]:
        name = row[1]
        maths = int(row[2])
        science = int(row[3])
        history = int(row[4])
        
        average = (maths + science + history) / 3
        
        # Write directly to the file, formatted to 2 decimal places
        outfile.write(f"{name}: {average:.2f}\n")

print("Report successfully generated using slicing!")
