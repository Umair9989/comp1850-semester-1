'''
This is a difficult activity which will involve some relatively challenging filtering/sorting of data
You will want to have the docs or a guide on using matplotlib/pandas available, it is not expected that you do this completely independently.
chatGPT is very good when debugging Pandas, as it decodes error messages into more readable explanations- so if you are struggling to understand what 
you have done wrong I recommend pasting error messages into it!

All the basic program code has been included, you should be able to simply write the code to filter the data into an appropriate dataframe and then
plot and show the graphs.
'''

import pandas as pd
import matplotlib.pyplot as plt

def average_bar_chart(data):
    '''
    Complete this code to produce a bar chart of the total of each 'hours per day' column
    '''
    hours_columns = ['Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day', 
                     'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day']
    averages = data[hours_columns].mean()
    averages.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.xlabel('Activity Type')
    plt.ylabel('Average Hours Per Day')
    plt.title('Average Hours Per Day by Activity')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def hours_histogram(data, column_name):
    '''
    Complete this code so that it can display a histogram of any given 'hours per day' column
    '''
    if column_name not in data.columns:
        print(f"Column '{column_name}' not found in data")
        return
    data[column_name].hist(bins=20, edgecolor='black', figsize=(10, 6))
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column_name}')
    plt.tight_layout()
    plt.show()

def hours_pie_chart(data, student_id):
    '''
    Complete this code so that it produces a pie chart of any given student's hours per day - this should be selected by student ID (the first column)
    '''
    if student_id < 0 or student_id >= len(data):
        print(f"Student ID {student_id} not found")
        return
    
    hours_columns = ['Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day', 
                     'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day']
    student_data = data.iloc[student_id][hours_columns]
    
    student_data.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 8))
    plt.title(f'Hours Distribution for Student {student_id}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

def total_hours_per_stress_level(data, stress_level):
    '''
    Complete this code to create a stacked bar chart showing a breakdown of the total hours worked by students, grouped by their reported stress level.
    '''
    if stress_level not in data['Stress_Level'].unique():
        print(f"Stress level '{stress_level}' not found in data")
        return
    
    hours_columns = ['Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day', 
                     'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day']
    
    filtered_data = data[data['Stress_Level'] == stress_level][hours_columns]
    totals = filtered_data.sum()
    
    totals.plot(kind='bar', figsize=(10, 6), color='coral')
    plt.xlabel('Activity Type')
    plt.ylabel('Total Hours')
    plt.title(f'Total Hours by Activity for {stress_level} Stress Level Students')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def display_menu():
    print("Student Lifestyle Data Analysis")
    print("1 - view average hours per day")
    print("2 - view specific activity")
    print("3 - view per-student breakdown")
    print("4 - view per stress level breakdown")
    print("Q - quit")
    choice = 0
    while choice not in ["1","2","3","4","Q"]:
        choice = input("Select option: ").upper()
    return choice


## main program:

data = pd.read_csv("lifestyle_data.csv")

# Note - when you run this in Interactive mode, the 'input' will be through a pop up instead of the terminal.
while True:
    choice = display_menu()
    match choice:
        case "Q":
            break
        case "1":
            average_bar_chart(data)
        case "2":
            col = input("Enter Hours Per column to analyse: ")
            hours_histogram(data, col)
        case "3":
            stid = int(input("Enter student ID: "))
            hours_pie_chart(data, stid)
        case "4":
            stress_level = input("Enter stress level: ").title()
            total_hours_per_stress_level(data, stress_level)
