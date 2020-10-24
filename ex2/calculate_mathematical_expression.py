#################################################################
# FILE : calculate_mathematical_expression
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Helping Greenfindor with math.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: -
# NOTES: -
#################################################################


def calculate_mathematical_expression(num1, num2, oper):
    """This function takes two numbers and operator and calculate the
    results or returns None for zero division error or not valid operator"""
    expression = ""
    if oper not in ["+", "-", "*", ":"]:  # check if operator is valid
        return None
    elif num2 == 0 and oper == ":":  # check for zeroDivision error
        return None
    else:  # Evaluate the expression
        if oper == "+":
            return num1 + num2
        if oper == "-":
            return num1 - num2
        if oper == "*":
            return num1 * num2
        if oper == ":":
            return num1 / num2


def calculate_from_string(string):
    """This function take string that represent simple mathematical
    expression and return the evaluated value with
     calculate_mathematical_expression"""
    OPER_INDEX = 0  # Constant for the index of the operator in the expression
    CHOSEN_OPER = ""  # Constant for the chosen operator as string
    if "+" in string:  # For finding the index of the operator
        OPER_INDEX = string.find("+")
        CHOSEN_OPER = "+"
    elif "-" in string:
        OPER_INDEX = string.find("-")
        CHOSEN_OPER = "-"
    elif "*" in string:
        OPER_INDEX = string.find("*")
        CHOSEN_OPER = "*"
    elif ":" in string:
        OPER_INDEX = string.find(":")
        CHOSEN_OPER = ":"
    else:
        return None  # Return None if the operator isn't valid
    num1 = float(string[:OPER_INDEX])  # for slice and convert the left
    num2 = float(string[OPER_INDEX + 1:])  # for slice and convert the right
    return calculate_mathematical_expression(num1, num2, CHOSEN_OPER)




