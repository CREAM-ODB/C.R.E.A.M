import turtle

#Setup
window = turtle.Screen()
window.title("Pong Project")
window.bgcolor("blue")
window.setup(width=690, height=420)
window.tracer(0)

# Score 
score_a = 0
score_b = 0

# Paddle A(left)
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape('square')
p_a.shapesize(stretch_wid=5,stretch_len=1)
p_a.color("white")
p_a.penup()
p_a.goto(-320,0)


# Paddle B(Right)
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape('square')
p_b.shapesize(stretch_wid=5,stretch_len=1)
p_b.color("white")
p_b.penup()
p_b.goto(310,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .15 # .15 pixel movements on x and y axis
ball.dy = .15

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,185)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 12, "normal"))


# Funtion paddle A
def p_a_up():
    y = p_a.ycor()
    y += 20
    p_a.sety(y)

def p_a_down():
    y = p_a.ycor()
    y -= 20
    p_a.sety(y)

# Funtion paddle B
def p_b_up():
    y = p_b.ycor()
    y += 20
    p_b.sety(y)

def p_b_down():
    y = p_b.ycor()
    y -= 20
    p_b.sety(y)

#binding 
window.listen()
window.onkeypress(p_a_up, "w")
window.onkeypress(p_a_down, "s")
window.onkeypress(p_b_up, "Up")
window.onkeypress(p_b_down, "Down")


#Main loop
while True:
    window.update()

    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarders
    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy *= -1 # reverse direction after border Hit

    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy *= -1 # reverse direction after border

    if ball.xcor() > 335:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Arial", 12, "normal"))

    if ball.xcor() < -335:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Arial", 12, "normal"))

    # Paddle Ball Collision
    if ball.xcor() > 310 and ball.xcor() < 320 and (ball.ycor() < p_b.ycor() + 50 and ball.ycor() > p_b.ycor() -50):
        ball.setx(310)
        ball.dx *= -1
    # seting left and right most limits for ball if collides with paddles pixel length reverse tragectory and if hit within
    # paddle width then reset to paddle edge and reverse trajectory

    if ball.xcor() < -320 and ball.xcor() > -330 and (ball.ycor() < p_a.ycor() + 50 and ball.ycor() > p_a.ycor() -50):
        ball.setx(-320)
        ball.dx *= -1
    