# NAME: YASMIEN GUILLERMO DEGUZMAN
# BLOCK: IV-BSIT-B
# ACTIVITY P4 - SAFE MENU PROGRAM
# DATE: NOV 27, 2026

# I used the show_menu() function to display the program menu. The purpose of using this function is to avoid writing the same code repeatedly. If i need the code I can simply call show_menu() whenever to display the menu again.
def show_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

# I used divide_numbers() to divide two numbers
def divide_numbers():

    try:
# I used input() to ask user to enter two numbers. I used float() so the user can enter numbers with or without decimal points
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))

# I used / to divide the first_num and second_num
        result = first_num / second_num

# I used ValueError to catch errors when the user enters letters.
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# I used ZeroDivisionError to preventing dividing by 0.
    except ZeroDivisionError:
        print("Cannot divide by zero!")

# I used else to display the results.
    else:
        print(f"Result: {result}")

# I used finnaly to display "Division operation finished."
    finally:
        print("Division operation finished.")


# I used open_file to open file.
def open_file():
    try:

# I used input() to ask user to enter the file name.
        file_name = input("Enter file name: ")
# I used open() to open file in read mode
        with open(file_name, "r") as file:
            content = file.read()
            print("\nFile Contents: ")
            print(content)

# I used FileNotFoundError to catch errors when the file does not exist and print "Error! File not found.".
    except FileNotFoundError:
        print("Error! File not found.")

# I used else when the file is successfully opened.
    else:
        print("File opened successfully.")

    finally:
        print("File operation finished.")


# I used main() to control the program.
def main():

# I used while loop to repeat the menu until user chooses to exit
    while True:
        show_menu()
        choice = input("Enter you want to choice: ")

# I used if_elif_else statements to check the user's choice and run the selected function. 
# If I chooce 1 the program will perform division.
        if choice == "1":
            divide_numbers()
# If I chooce 2 the program will open a file.
        elif choice == "2":
            open_file()
# If I chooce 3 the program will exit.
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
# If I enter a number that is not in the choices, the program will display "Invalid choice! Please select 1, 2, or 3."
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()

# EXPLANATION
# I learned how ValueError, ZeroDivisionError, and FileNotFoundError work.
# I learned that ValueError handles invalid inputs, ZeroDivisionError prevents division by zero, and FileNotFoundError handles missing files.
# In this activity helped me understand how to handle different errors and make my program work properly.

