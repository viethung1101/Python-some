#!/usr/bin/env python3

import turtle
score_a = 0
score_b = 0
#set up window for player
wn = turtle.Screen()
wn.title("Pong Game by January")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")









#main game loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection = ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection*-1
    if ball.xcor()<-390:
        ball.setx(-390)
        ballxdirection = ballxdirection*-1
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=('Arial',24,'normal'))
    if ball.xcor()>390:
        ball.setx(390)
        ballxdirection = ballxdirection*-1
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=('Arial',24,'normal'))

    if (ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40) and (ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ballxdirection = ballxdirection * -1

    if (ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40) and (ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
