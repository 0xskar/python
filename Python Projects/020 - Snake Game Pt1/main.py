from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Wicked awesome snake game of doom.")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# TODO CREATE MOVEMENT FUNCTIONS
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_movement()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for body in snake.bodies[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
