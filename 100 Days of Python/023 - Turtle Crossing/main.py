import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.up, key="Up")
car = CarManager()
scoreboard = Scoreboard()

starting_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(starting_speed)
    screen.update()

    car.create_car()
    car.car_moving()

    for c in car.cars:
        if c.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.next_level()
        player.next_level()
        starting_speed -= 0.02



screen.exitonclick()
