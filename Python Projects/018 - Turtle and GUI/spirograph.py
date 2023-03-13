import turtle as t
from turtle import Screen
import random

# spirograph of circles
# radius 100 in distance
# random colors each circle

turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)
turtle.pensize(5)


def random_color():
    the_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return the_color


for _ in range(72):
    turtle.color(random_color())
    turtle.circle(200)
    turtle.setheading(turtle.heading() + 5)

screen = Screen()
screen.exitonclick()
