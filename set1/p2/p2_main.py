# NAME: YASMIEN GUILLERMO DE GUZMAN
# BLOCK: IV-BSIT-B
# ACTIVITY P2 - STUDENT UTILITIES MODULE
# DATE: NOV 26, 2026

# I used import datetime to access the datetime module. 
# This allow to get the current date and time when the student grade report is generated
import datetime

# I used import student_utils to access the functions stored in the student_utils.py file.
import student_utils

# I used from student_utils import to import specific functions from the student_utils.py.
# I imported check_status, get_highest, and get_lowest so I can call these functions directly without writing student_utils before each function name.
from student_utils import check_status, get_highest, get_lowest

def main():

    print("=====STUDENT UTILITIES MODULE=====")
    print("Ms. Yasmien Guillermo De Guzman")
# I used input() to ask student how many grades they want to enter.
# The number_of_grades variable store how many grades will ask the student to enter.
    number_of_grades = int(input("\nHow many grades do you want to enter? "))

# I used grades = [] to store the grades entered by the student.
    grades = []

# I used a For Loop to repeat a block of code.
# I used range(number_of_grades) to determines how many times the program will ask for a grade.
    for i in range(number_of_grades):
        grade = float(input("Enter grade " + str(i + 1) + ": "))
        grades.append(grade)

#This part will display the grades report on your screen together with the output.
    print("\n=======STUDENT GRADE REPORT=======")

    print("Highest: ", get_highest(grades))
    print("Lowest: ", get_lowest(grades))
    print("Average: ", student_utils.calculate_ave(grades))
    print("Status: ", check_status(grades))

    report_date = datetime.datetime.now()

    print("\nReport Generated: ", report_date)
    print("==================================")


main()

# Explanation
# I learned how to use modules and functions in Python to make my program more organized. 
# I used the student_utils.py file to access functions that find the highest and lowest grades, calculate the average, and check the student's status. 
# I also learned how to use import and from__import to access functions from another Python file.
# I used the datetime module to display the current date and time when the student grade report is generated. Through this activity, I understood how modules help make code reusable and easier to manage.
# In this code, I learned how the datetime module works. It was also discussed in our online lesson, but I did not fully understand the last part of the output. I was not sure if the numbers after yr-m-d (18:33:28.578985) represented milliseconds or something else. But now, I understand how the datetime output works.
