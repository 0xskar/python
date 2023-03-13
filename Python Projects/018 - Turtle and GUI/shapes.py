from turtle import Turtle, Screen
import random

pen = Turtle()


def shape(sides, side_length):
    """ takes the sides and side length of the shape and draws that shape """
    shape_angle = 360 / sides
    for side in range(sides):
        pen.forward(side_length)
        pen.right(shape_angle)


shapes = 5
colors = ["blue", "red", "coral", "DarkOrange", "DeepPink", "green", "lawngreen", "chocolate", "aquamarine"]

for shape_sides in range(3, 11):
    pen.pencolor(random.choice(colors))
    pen.fillcolor(random.choice(colors))
    shape(shape_sides, 100)


screen = Screen()
screen.exitonclick()
