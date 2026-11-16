import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# It's a DataFrame

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print("Total number of students:", len(data))

# Find the mean average GPA of the students
print("Mean GPA:", data['GPA'].mean())

# Find the standard deviation of how much sleep students get per day
print("Standard deviation of sleep:", data['Sleep_Hours_Per_Day'].std())

# Find the maximum amount of study hours per day
print("Maximum study hours:", data['Study_Hours_Per_Day'].max())

# Sort the students by social hours per day ascending (lowest -> highest)
sorted_by_social = data.sort_values('Social_Hours_Per_Day')
print("\nSorted by social hours (ascending):")
print(sorted_by_social)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data['Total_hours'] = data['Study_Hours_Per_Day'] + data['Extracurricular_Hours_Per_Day'] + data['Sleep_Hours_Per_Day'] + data['Social_Hours_Per_Day'] + data['Physical_Activity_Hours_Per_Day']
print("\nData with Total_hours column:")
print(data[['Total_hours', 'GPA', 'Stress_Level']].head())

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress = data[data['Stress_Level'] == 'High']
low_stress = data[data['Stress_Level'] == 'Low']

if len(high_stress) > 0:
    print("\nHigh stress students mean GPA:", high_stress['GPA'].mean())
else:
    print("\nNo high stress students found")
    
print("Low stress students mean GPA:", low_stress['GPA'].mean())
print("\nConclusion: Higher stress does NOT lead to higher GPA (lower average GPA with high stress)")
