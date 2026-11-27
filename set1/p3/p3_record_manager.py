# NAME: YASMIEN GUILLERMO DE GUZMAN
# BLOCK: IV-BSIT-B
# ACTIVITY P3 - STUDENT RECORD MANAGER
# DATE: NOV 26, 2026

# I used a list to store the names of the Students.
students = []

# I used a set to keep track of student names and prevent duplicates.
student_names = set()

def add_student():

# I used input() to ask the user to enter his/her name.
    student_name = input("Enter student name: ")

# I used if to check if the name is empty.
    if student_name == "":
        print("Please enter student name.")

# I used elif and lower() to check for duplicate names and when name is duplicate it will print "Student already exists!"
    elif student_name.lower() in student_names:
        print("Student already exists!")

# I used append() to add the student name to the list.
    else:
# I used append() to add the student name to the list.
        students.append(student_name)

# I used add() to add the lowercase name to the set.
        student_names.add(student_name.lower())

        print("Student added successfully!")


def remove_student():

    student_name = input("Enter student name you want to remove: ")

# I used if to check if the name exists.
    if student_name.lower() in student_names:

# I used for to find the student in the list
        for student in students:

            if student.lower() == student_name.lower():

# I used remove() to remove or delete the student name from the list.
                students.remove(student)
# I used remove() and lower() to remove or delete the student name from the set.
                student_names.remove(student.lower())

                print("Student removed successfully!")
                break
    else:
        print("Student not found!")


def search_student():

# I used input() to ask the student to search the name.
    search_name = input("Enter student name you want to search: ")  

# I used found = False variable to check if a student is found.
    found = False

# I used for to check each student in the list.
    for student in students:

# I used lower() and in to search for a partial name.
        if search_name.lower() in student.lower():
            print("Student found: ", student)
            found = True

# I used if to display a messege if no student is found.
    if found == False:
        print("Student not found!")


def display_students():

    print("\n=====STUDENT LIST=====")

# I used if to check if the list is empty.
    if len(students) == 0:
        print("No students to display.")

    else:
# I used sort() to arrange the student names alphabetically.
        students.sort()

# I used len() to display the total number of students. 
        print("Total Students: ", len(students))

# I used range() to display the students with numbers.
        for i in range(len(students)):
            print(i + 1, ".", students[i])


def main():

    while True:

        print("\n=====STUDENT RECORD MANAGER=====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

# I used imput() to ask the student to select an option.
        choice = input("Enter you want to proccess: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Invalid! Please try again.")

main()

# Explanation
# In this program I learned the  difference between list and set. 
# A list can store multiple student names and keep their order. I  used a list to store and display the names of the students.
# A set store unique values and does not allow duplicate entries. I usedd a set to prevent duplicate student names in my program.
# 