#################################################################
# FILE : math_print.py
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that make some basic math.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: https://docs.python.org/3/library/math.html
# NOTES: -
#################################################################
import math


def golden_ratio():
    #This function print the golden ratio!
    print((1 + math.sqrt(5))/2)


def six_squared():
    #This function return the result of 6 to the power of 2
    print(6 ** 2)


def hypotenuse():
    #Function print the length of the hypotenuse in right angled triangle
    print(math.sqrt(5 ** 2 + 12 ** 2))


def pi():
    #Function print the value of pi
    print(math.pi)


def e():
    # Function print the value of e
    print(math.e)


def squares_area():
    #Function print the sequence of areas of squares with sides
    #from 1 to 10
    print(1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
