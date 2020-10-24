#################################################################
# FILE : calculate_mathematical_expression
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Solving quadratic equation.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: -
# NOTES: -
#################################################################

import math


def equation_quadratic(a, b, c):
    """This function solve quadratic equation and return the solution in
    tuple (solution1, solution2). if there are no solutions the function return
    (None, None) and if there is only one solution it  returns (solution1,None)
    """
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return -b / 2, None
    elif discriminant > 0:
        return (-b + math.sqrt(discriminant)) / 2, (-b - math.sqrt(discriminant)) / 2


def quadratic_equation_user_input():
    """This function takes numbers a, b, c from user and solve the quadratic
     equation represented by the parameters by calling equation_quadratic """
    coefs = input("Insert coefficients a, b, and c:")
    coefs = coefs.split(" ")
    if int(coefs[0]) == 0:
        return "The parameter 'a' may not equal 0"
    a = int(coefs[0])
    b = int(coefs[1])
    c = int(coefs[2])
    result = equation_quadratic(a, b, c)
    solution1 = result[0]
    solution2 = result[1]
    if (None, None) == result:
        return "The equation has no solutions"
    elif result[1] is None:
        return f"The equation has 1 solution: {solution1}"
    else:
        return f"The equation has 2 solution: {solution1} and {solution2}"

