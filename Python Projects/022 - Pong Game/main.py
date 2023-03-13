from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Wicked Awesome Pong Game")
screen.tracer(0)

paddle_left = Paddle((-360, 0))
paddle_right = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")
screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.moving()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() > -360:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.move_speed = 0.1
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -400:
        ball.move_speed = 0.1
        scoreboard.right_point()
        ball.reset_position()

screen.exitonclick()
