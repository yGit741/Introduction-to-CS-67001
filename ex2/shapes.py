#################################################################
# FILE : calculate_mathematical_expression
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Helping Harry Potter calculating areas of Shapes.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED:
# NOTES: -
#################################################################


import math


def circle_area():
    """Get radius from user and return the area of a circle"""
    radius = float(input(""))
    return math.pi * (radius ** 2)


def rectangle_area():
    """Get edges from user and return the area of a rectangle"""
    edge_1 = float(input(""))
    edge_2 = float(input(""))
    return edge_1 * edge_2


def triangle_area():
    """Get edge from user and return the area of a equilateral triangle"""
    edge = float(input(""))
    return (math.sqrt(3)/4) * edge ** 2


def shape_area():
    """Get inputs from user and depend on the number it gives the function
    demands other inputs for calculating the area of the shape represented by
    the first number given."""
    shape = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape == 1:
        return circle_area()
    elif shape == 2:
        return rectangle_area()
    elif shape == 3:
        return triangle_area()