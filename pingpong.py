import turtle

screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("darkblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle size, shape, location

paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

# Paddle 1 controls

def paddle_1_up():
    y = paddle_1.ycor()
    y = y+10
    paddle_1.sety(y)
    if y > 240:
        paddle_1.sety(240)

def paddle_1_down():
    y = paddle_1.ycor()
    y = y-10
    paddle_1.sety(y)
    if y < -230:
        paddle_1.sety(-230)        

# Paddle 2 controls

def paddle_2_up():
    y = paddle_2.ycor()
    y = y+10
    paddle_2.sety(y)
    if y > 240:
        paddle_2.sety(240)    

def paddle_2_down():
    y = paddle_2.ycor()
    y = y-10
    paddle_2.sety(y)
    if y < -230:
        paddle_2.sety(-230)    

# Paddke Keys

screen.listen()
screen.onkeypress(paddle_1_up,"a")
screen.onkeypress(paddle_1_down,"z")
screen.onkeypress(paddle_2_up,"k")
screen.onkeypress(paddle_2_down,"m")

while(1):
    screen.update()

