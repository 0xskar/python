from turtle import Turtle

PADDLE_HEIGHT = 5
MOVEMENT_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(name="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_HEIGHT)
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.forward(MOVEMENT_DISTANCE)

    def down(self):
        self.backward(MOVEMENT_DISTANCE)
