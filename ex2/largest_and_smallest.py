#################################################################
# FILE : calculate_mathematical_expression
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Helping Dumbledore and Mcgonagall finding easiest and hardest
# spell.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: -
# NOTES: -
#################################################################

def largest_and_smallest(num1, num2, num3):
    """This function takes three numbers and return tuple with (max,min)"""
    if num1 >= num2:
        hardest = num1
        easiest = num2
        if num1 <= num3:
            hardest = num3  # Because: num3 >= num1 >= num2
        if num2 >= num3:
            easiest = num3  # Because: num1 >= num2 >= num3
    else:  # Which mean num1 < num2
        hardest = num2
        easiest = num1
        if num2 <= num3:
            hardest = num3  # Because: num3 >= num2 > 1
        if num1 >= num3:
            easiest = num3  # Because: num2 > num1 >= num3
    return hardest, easiest


def check_largest_and_smallest():
    """This function will check that largest_and_smallest works as expected
    with variety of inputs """
    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    if largest_and_smallest(0, 0, 0) != (0, 0):
        return False
    if largest_and_smallest(-3, -2, -1) != (-1, -3):
        return False
    return True



