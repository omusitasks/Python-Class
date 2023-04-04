import sys

# Set up grades and their corresponding GPA values
grades = {
    'A':4.0, 
    'A-':3.66, 
    'B+':3.33, 
    'B':3.0, 
    'B-':2.66, 
    'C+':2.33, 
    'C':2.0, 
    'C-':1.66, 
    'D+':1.33, 
    'D':1.00, 
    'D-':.66, 
    'F':0.00
}



# Get letter grades from command line arguments
letter_grades = []
for arg in sys.argv[1:]:
    letter_grade = arg.upper()
    letter_grades.append(letter_grade)

# Ensure at least one grade is provided
if len(letter_grades) == 0:
    letter_grade = input("Please enter at least one grade: ")
    letter_grade = letter_grade.upper()
    letter_grades.append(letter_grade)

# Calculate GPA
total = 0
for letter_grade in letter_grades:
    total += grades[letter_grade]
gpa = total / len(letter_grades)

# Print GPA
print('My GPA is {:.2f}'.format(gpa))