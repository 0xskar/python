from turtle import Screen
import turtle as t
import random


def random_color():
    ran_col = random.choice(color_tuples)
    return ran_col


class Draw:
    def __init__(self, size):
        self.rows = size
        self.columns = size
        self.dot_size = 40

    def create_row(self):
        for column in range(self.columns):
            turtle.color(random_color())
            turtle.dot(self.dot_size)
            if column < self.columns - 1:
                turtle.forward(self.dot_size * 2)

    def create(self):
        for rows in range(self.rows):
            turtle.goto(starting_position[0], starting_position[1])
            self.create_row()
            starting_position[1] += self.dot_size * 2



# REQUIREMENTS
# 10 x 10 Rows of dots
# each dot 20 in size, spaces apart by 50 units
# TODO Create function that places 10 dots 20 in size spaced apart by 50 units
#  then returns to original position but 50 units up

color_tuples = [(40, 26, 13), (112, 100, 57), (19, 125, 147), (195, 221, 232), (29, 50, 30), (65, 106, 86),
                (238, 232, 220), (183, 160, 109), (74, 74, 34), (105, 191, 215), (157, 139, 73), (28, 10, 14),
                (14, 28, 35), (35, 82, 65), (133, 211, 234), (8, 95, 108), (211, 226, 219), (42, 163, 189),
                (138, 168, 157), (234, 205, 95), (95, 146, 129), (239, 229, 233), (98, 50, 37), (170, 204, 195),
                (106, 68, 77), (103, 40, 50), (171, 162, 166), (56, 55, 86), (171, 112, 92), (204, 186, 183),
                (244, 212, 6), (169, 194, 220), (205, 185, 189), (107, 127, 154), (173, 95, 108)]
starting_position = [-400, -370]
turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
grid = Draw(10)
grid.create()
screen = Screen()
screen.exitonclick()
print(screen.screensize())
