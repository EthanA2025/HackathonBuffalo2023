import csv
import numpy as np

np.random.seed(42)

num_students = 20000
num_years = 8
gpa_mean = 2.5
gpa_std = 1
data = []

# Generate the data for each student
for i in range(num_students):
    # Generate GPA values
    gpa_values = np.round(np.clip(np.random.normal(gpa_mean, gpa_std, num_years), 0, 4), decimals=2)
    
    # Compute the average GPA
    avg_gpa = np.mean(gpa_values)
    
    # Determine the dropout status
    dropout = 1 if avg_gpa <= 1.5 else 0
    
    # Append the student's data to the list
    data.append([i+1] + list(gpa_values) + [dropout])

# Define the column headers
headers = ['student_id'] + [f'gpa_year_{i+1}' for i in range(num_years)] + ['dropout']
<<<<<<< HEAD
#f'gpa_year_{i+1}' for i in range(num_years)
=======
#
>>>>>>> 6105fa0410e5a1ef03f0607e66901cfc1ad8454e
# Write the data to a CSV file
with open('student_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)