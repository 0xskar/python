from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[0]

    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.bodies.append(new_snake)

    def extend(self):
        self.add_segment(self.bodies[-1].position())

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def snake_movement(self):
        for body in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[body - 1].xcor()
            new_y = self.bodies[body - 1].ycor()
            self.bodies[body].goto(x=new_x, y=new_y)
        self.bodies[0].forward(MOVE_DISTANCE)





    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
