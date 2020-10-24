#################################################################
# FILE : hello_turtle.py
# WRITER : Yonatan Greenshpan , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that draw a nice garden
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: https://stackoverflow.com/questions/32180949/turtle-module-in-python-not-importing
# NOTES: -
#################################################################
import turtle


def draw_petal():
    # This function draws a single petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    # This function draws a flower by multiples calls to draw_petal
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    # This function draws a flower and advance the turtle to the next starting point
    draw_flower()
    turtle.right(90)
    turtle.penup()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.pendown()


def draw_flower_bed():
    turtle.penup()
    turtle.forward(200)
    turtle.left(180)
    turtle.pendown()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done()
