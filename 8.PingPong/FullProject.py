import turtle


screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("Blue")
screen.setup(width=800, height=600)
screen.tracer(0)


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

ball = turtle.Turtle()
ball.shape("circle")
ball.color("Green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

score1= 0
score2= 0
scoreText = turtle.Turtle()

scoreText.color("white")
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(0,260)
scoreText.write("Player 1 : 0  Player 2 : 0", align="center", font=("Courier",22,"normal"))
step = 10

def moveBall():
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    x = ball.xcor()
    y = ball.ycor()
    
    if x>390:
        ball.setx(390)
        ball.dx = ball.dx * -1
    if x <-390:
        ball.setx(-390)
        ball.dx = ball.dx * -1
    
    if y >290:
        ball.sety(290)
        ball.dy = ball.dy * -1
        
    if y <-290:
        ball.sety(-290)
        ball.dy =ball.dy * -1
        
        

  
    

def paddle_1_up():
    y = paddle_1.ycor()
    y = y+step
    paddle_1.sety(y)
    if  y > 240:
        paddle_1.sety(240)
    
def paddle_1_down():
    y = paddle_1.ycor()
    y = y-step
    paddle_1.sety(y)
    if y<-240:
        paddle_1.sety(-240)
        
def paddle_1_right():
    x =  paddle_1.xcor()
    x= x+step
    paddle_1.setx(x) 
    if x >-10:
        paddle_1.setx(-10)

def paddle_1_left():
    x =  paddle_1.xcor()
    x= x-step
    paddle_1.setx(x) 
    if x <-350:
        paddle_1.setx(-350)

def paddle_2_left():
    x =  paddle_2.xcor()
    x= x-step
    paddle_2.setx(x) 
    if x <10:
        paddle_2.setx(10)

def paddle_2_right():
    x =  paddle_2.xcor()
    x= x+step
    paddle_2.setx(x) 
    if x >350:
        paddle_2.setx(350)        


def paddle_2_down():
    y = paddle_2.ycor()
    y = y-step
    paddle_2.sety(y)
    if y<-240:
        paddle_2.sety(-240)

def paddle_2_up():
    y = paddle_2.ycor()
    y = y+10
    paddle_2.sety(y)
    if  y > 240:
        paddle_2.sety(240)
        
        

def checkCollision():
    if (paddle_1.xcor()+20 >=  ball.xcor() >= paddle_1.xcor()-20) and (paddle_1.ycor()+60 >=  ball.ycor() >= paddle_1.ycor()-60):
        ball.dx = ball.dx*-1
        ball.dy = ball.dy *-1
        
        x = ball.xcor()
        x= x+10
        ball.setx(x)
    
    if (paddle_2.xcor()+20 >=  ball.xcor() >= paddle_2.xcor()-20) and (paddle_2.ycor()+60 >=  ball.ycor() >= paddle_2.ycor()-60):
        ball.dx = ball.dx*-1
        ball.dy = ball.dy *-1
        
        x = ball.xcor()
        x= x-10
        ball.setx(x)  
    
    
screen.listen()
screen.onkeypress(paddle_1_up,"w")
screen.onkeypress(paddle_1_down,"s")
screen.onkeypress(paddle_1_right,"d")
screen.onkeypress(paddle_1_left,"a")
screen.onkeypress(paddle_2_up,"Up") 
screen.onkeypress(paddle_2_down,"Down")
screen.onkeypress(paddle_2_right,"Right")
screen.onkeypress(paddle_2_left,"Left")
while(1):
    screen.update()
    moveBall()
    checkCollision()
    if ball.xcor()>=350:
        score1 = score1 +1
        scoreText.clear()
        scoreText.write("Player 1 : {}  Player 2 : {}".format(score1,score2), align="center", font=("Courier",22,"normal"))
        ball.goto(0,0)
        ball.dx = ball.dx *-1
        
    if ball.xcor()<-350:
        score2 = score2 +1
        scoreText.clear()
        scoreText.write("Player 1 : {}  Player 2 : {}".format(score1,score2), align="center", font=("Courier",22,"normal"))
        ball.goto(0,0)
        ball.dx = ball.dx *-1        
    