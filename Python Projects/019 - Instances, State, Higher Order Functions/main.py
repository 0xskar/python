import turtle
from turtle import Turtle, Screen
import random

is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Choose Winner", prompt="Which color turtle will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# TODO create turtle for every color and set starting position
for color in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[color])
    new_turtle.goto(x=-220, y=y_positions[color])
    all_turtles.append(new_turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_racing = False
            if winning_color == user_bet:
                print(f"You win, {winning_color} was the winner!")
            else:
                print(f"You lose, {winning_color} was the winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
