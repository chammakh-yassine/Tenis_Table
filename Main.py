# this is a simple football game using Turtle library.


import turtle     #import Turtle
import math       #import math

from Control import Control,Ball    #import control and ball classes from Control.py
from Player import GameObjects    #the player class that we made to setup our players

def Borders():                    # draw the borders
    border=turtle.Turtle()
    border.speed(0)
    border.shape('circle')
    border.color('white')
    border.pencolor('white')
    border.shapesize(0.01)
    border.pensize(4)
    border.penup()
    border.goto(-800,370)
    border.pendown()
    border.goto(800,370)
    border.penup()
    border.goto(800, -370)
    border.pendown()
    border.goto(-800,-370)
    border.penup()
    border.goto(0,370)
    border.pendown()
    border.goto(0,-100)
    border.circle(100)
    border.goto(0,-370)

# make the game screen and change the size
screen=turtle.Screen()
screen.tracer(0)     # screen will not updated automatically
screen.bgcolor('green')
screen.setup(800,600)
# make the first player
player1=GameObjects('red',-730,0)
player2=GameObjects('blue',730,0)
# Show the ball in our game
ball = GameObjects('white',0,0)
ball.player.shape('circle')
ball.player.speed(0)
#call the method "Show_Player" in purpose to show the player on the right position in screen
player1.Show_Player()
player2.Show_Player()
Borders()   # call the Borders function
#make the input and control of the first player and second player // maybe the Control  class

control1=Control(player1,1)
control2=Control(player2,2)
ballcontrol = Ball(ball)    # make a Ball object so we can move the ball

while(True):
    if abs(ball.player.xcor()) >= 752:     # the end of our gameloop
        break
    ballcontrol.move()                                # move the ball
    turtle.listen()                              # waiting for input
    control1.take_input()                       #save input player 1
    control2.take_input()                        #save input second player
    if abs(player1.player.ycor())<300:             #if the else between my boundaries
        control1.move()                            # move the player
    else:
        check = lambda j:j-20 if j>0 else j+20            #change the y coordination of my player
        player1.player.sety(check(player1.player.ycor()))
    if abs(player2.player.ycor()) <= 300:
        control2.move()
    else:
        check = lambda j: j - 20 if j > 0 else j + 20
        player2.player.sety(check(player2.player.ycor()))

     #check if the ball hit on of the players but only on x axis
    checkXcordinate2 = math.ceil(player2.player.xcor() - 15) <= math.ceil(ball.player.xcor())
    checkXcordinate1=math.ceil(player1.player.xcor() + 15) >= math.ceil(ball.player.xcor())


    if checkXcordinate2 and ballcontrol.checkYcordinate(player2)  :    # the second part of the statment check if the ball hit the player on same y axes
        ballcontrol.change_direction()
    if checkXcordinate1 and ballcontrol.checkYcordinate(player1) :
        ballcontrol.change_direction()

    turtle.update()    # update the screen



