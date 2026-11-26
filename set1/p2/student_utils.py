# NAME: YASMIEN GUILLERMO DE GUZMAN
# BLOCK: IV-BSIT-B
# ACTIVITY P2 - STUDENT UTILITIES MODULE
# DATE: NOV 26, 2026

#  I used get_highest function to find the highest grade in the list.
def get_highest(grades):
    return max(grades)

# I used get_lowest function to find the lowest grade in the list.
def get_lowest(grades):
    return min(grades)

# I used calculate_ave function to calculate the average of all the grade entered by the student.
def calculate_ave(grades):
    average = sum(grades) / len(grades)
    return average

# I used check_status function to check if the student average is PASSED or FAILED.
def check_status(grades):
    average = calculate_ave(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"