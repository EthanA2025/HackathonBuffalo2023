import csv
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Define the number of students and years
num_students = 20000
num_years = 4

# Define the GPA mean and standard deviation
gpa_mean = 3.0
gpa_std = 0.8

# Create an empty list to store each student's data
data = []

# Generate the data for each student
for i in range(num_students):
    # Generate GPA values
    gpa_values = np.clip(np.random.normal(gpa_mean, gpa_std, num_years), 0, 4)
    
    # Compute the average GPA
    avg_gpa = np.mean(gpa_values)
    
    # Determine the dropout status
    dropout = 1 if avg_gpa <= 1.5 else 0
    
    # Append the student's data to the list
    data.append([i+1] + list(gpa_values) + [dropout])

# Define the column headers
headers = ['student_id'] + [f'gpa_year_{i+1}' for i in range(num_years)] + ['dropout']

# Write the data to a CSV file
with open('student_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
