
# 1) Run the code: Execute the code by pressing the "Run" button.
# 2) Enter branch/section names and data: Input the branch names and the number of present and absent students for each branch.
# 3) View the plot: After entering the data, a plot will be displayed showing the attendance for each branch.
# 4) Analyze the plot: Look at the bars to see the attendance status for each branch.
# 5) Close the plot: Once you're done, close the plot window.



import pandas as pd
import matplotlib.pyplot as plt
import math

# Function to plot data for each branch
def plot_branch_data(branch, present, absent):
    total = present + absent
    # Plotting
    plt.bar(['Present', 'Absent'], [present, absent], color=['skyblue', 'salmon'])
    plt.title(f'Student Attendance in {branch}')
    plt.xlabel('Status')
    plt.ylabel('Number of Students')
    # Annotate bars with exact numbers
    plt.text(0, present, str(present), ha='center', va='bottom')
    plt.text(1, absent, str(absent), ha='center', va='bottom')
    # Mark the creator
    plt.text(0.5, total/2,' ', ha='center', va='center', color='black', fontsize=10)
    # plt.text(0.5, total/2, 'Made by Kundan Singh Rautela', ha='center', va='center', color='black', fontsize=10)

# Get input for branches from the user
branches = input("Enter the names of branches/Section separated by commas (CSE, DS, AI, IOT, Others): ").split(',')

# Dictionary to store branch data
branch_data = {}

# Get input for each branch
for branch in branches:
    print(f"Enter data for branch: {branch}")
    present_students = int(input("Number of students present: "))
    absent_students = int(input("Number of students absent: "))
    total_students = present_students + absent_students
    branch_data[branch] = {'Total': total_students, 'Present': present_students, 'Absent': absent_students}

# Plotting
num_branches = len(branches)
num_rows = math.ceil(num_branches / 3)  # Maximum 3 columns
plt.figure(figsize=(12, 4 * num_rows))
for i, (branch, data) in enumerate(branch_data.items(), 1):
    plt.subplot(num_rows, min(3, num_branches), i)
    plot_branch_data(branch, data['Present'], data['Absent'])

# Mark the creator at the bottom-right corner of the page
plt.text(2, -10 * num_rows, '-------Made by Kundan Singh Rautela', ha='right', va='bottom', color='black', fontsize=10)

# Adjust layout and display
plt.tight_layout()
plt.show()


