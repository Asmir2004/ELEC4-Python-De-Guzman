# NAME: YASMIEN GUILLERMO DE GUZMAN
# BLOCK: IV-BSIT-B
# ACTIVITY 1 - STUDENTS GRADE CALCULATOR
# DATE: NOV 25, 2026

# I used global variable (grades) to store the grades entered by the student. 
# I used empty list ([]) to store the multiple grades or value in the grades_list = [].
# For example, if the student enters 5 grades: 99, 98, 96, 97, and 95, 
# the list will look like this grades = [99, 98, 96, 97, 95].
grades = []


# I used the enter_grades() fuction to accept the grades entered by the student.
def enter_grades():

    grades_list = []
    number = int(input("How many grades do you want to  enter? "))

# I used a While Loop to repeatedly execute statements as long as the condition is true.
# If the student enter 0 or negative number, the output will be "Please enter at least 1 grade." thats why I use a while loop to prevent the student from entering zero or a negative number of grades and asks for another input.
# This prevents the student from entering an invalid number of grades.
    while number <= 0:
        
        print("Please enter at least 1 grade.")
        number = int(input("How many grades do you want to calculate?"))


# I used a For Loop to repeat a block of code. 
# Since we do not know how many grades the students wants to enter.  
# range(number) determines how many time the program will askk for a grade.
    for i in range(number):

        grade = float(input("\nEnter grade" + str(i + 1) + ": "))

# I used a while loop to validate the entered grade. If the grade is below 0 or above 100, the program ask the student to enter another grade until a valid grade is provided.
        while grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            grade = float(input("Enter grade" + str(i + 1) + ": "))

        grades_list.append(grade)

    return grades_list

# I used the calculate_ave() function to calculate the average of all the grades entered by the students. The purpose of parameter is to receive a list of grades to calcu the average.
def calculate_ave(grades):
    
    total = 0


# I used a For Loop to access eash grade and add it to the total
    for grade in grades:
        total = total + grade

# I used len() to count the number of grades in the list.
# It divided the total by the number of grades to get the average.
    average = total / len(grades) 

    return average

# I used the get_highest function to find the highest grade in the list.
def get_highest(grades):

    highest = grades[0]

# I used a For Loop to compare each grade in the list
    for grade in grades:

# I used an if statement to check if the current grade is higher than the current highest value.
        if grade > highest:
            highest = grade

    return highest

# I used the get_lowest function to find the lowest grade in the list.
def get_lowest(grades):

    lowest = grades[0]

    for grade in grades:

# I used an if statement to check if the current grade is lower than the current lowest value.
        if grade < lowest:
            lowest = grade

    return lowest

# I used an if-else statement to determine if PASS or FAIL based on the average grade.
def get_status(grades):

    average = calculate_ave(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

# I used the display_results function to display the calculated results on the screen.
def display_results(grades):

    if len(grades) > 0:

        average = calculate_ave(grades)
        highest = get_highest(grades)
        lowest = get_lowest(grades)
        status = get_status(grades)

        print("\n===================RESULTS===================")
        print("Average: " + str(round(average, 2)))
        print("Highest: " +str(highest))
        print("Lowest: " +str(lowest))
        print("Status: " + str(status))

    else:
        print("\nNo grades entered yet.")

while True:

    print("\n=============STUDENT GRADE CACULATOR=============")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")

    choice = input("\nEnter choice:")

    if choice == "1":

        grades = enter_grades()
        print("\nGrades successfully entered!")

    elif choice == "2":

        display_results(grades)

    elif choice == "3":

        print("\nThank you for using Student Grade Calculatoor!")

        break
    else:
        print("\nInvalid choice. Please try again.")


# Explanation
# A global variable is declared outside a function. 
# In this program, grades is a global variable because it is declared outside the functions. 
# Local variable are declared inside a function like for example grades_list, number, and highest these are the local variable only accessible inside the function where they are declared.
# While fixing my code, I noticed that when using VSCodium, even if the code is correct, an IndentationError can still occur. That is why it is important to know which statements should be indented inside or placed outside the while, for, and if statements 
