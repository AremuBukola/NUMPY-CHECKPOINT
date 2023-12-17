#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def calculate_grades():
    # Get the number of students and subjects from the user
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    # Initialize an empty array to store the student marks
    marks_array = np.zeros((num_students, num_subjects), dtype=float)

    # Get marks for each student in each subject
    for i in range(num_students):
        print(f"\nEnter marks for Student {i + 1}:")
        for j in range(num_subjects):
            marks_array[i, j] = float(input(f"Enter marks for Subject {j + 1}: "))

    # Calculate total marks, percentage, and grade for each student
    total_marks = np.sum(marks_array, axis=1)
    percentage = (total_marks / (num_subjects * 100)) * 100  # Assuming each subject has a maximum of 100 marks
    grades = np.where(percentage >= 90, 'A',
                      np.where(percentage >= 80, 'B',
                               np.where(percentage >= 70, 'C',
                                        np.where(percentage >= 60, 'D', 'F'))))

    # Display the results in a tabular format
    print("\nResults:")
    print("------------------------------------------------------")
    print("Student\t| Total Marks\t| Percentage\t| Grade")
    print("------------------------------------------------------")
    for i in range(num_students):
        print(f" {i + 1}\t| {total_marks[i]}\t\t| {percentage[i]:.2f}%\t\t| {grades[i]}")

# Run the program
calculate_grades()

