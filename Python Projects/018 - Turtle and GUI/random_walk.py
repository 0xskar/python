from turtle import Screen
import turtle as t
import random

n_steps = 10000
l_steps = 30
size = 15
# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1
speed = 0

walker = t.Turtle()
t.colormode(255)
walker.pensize(size)
walker.hideturtle()
walker.speed(speed)

walk_angles = [0, 90, 180, 270]


def random_color():
    random_colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_colors


def walk(steps, step_size):
    """ takes how many steps to walk then performs a random walk """
    for _ in range(steps):
        # TODO make it change a random rgb color
        walker.color(random_color())
        walker.forward(step_size)
        walker.right(random.choice(walk_angles))


walk(n_steps, l_steps)

screen = Screen()
screen.exitonclick()
