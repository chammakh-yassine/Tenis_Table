# control class to make the control inputs
import turtle
import math
import random
from itertools import count
from random import randrange


class Control:

    def __init__(self, Player,Id):     # constractor
        self.Player=Player
        self.id=Id
        self.key_states = {}   # to save the inputs from the player

    def on_key_press(self,key):         #if the key pressed take the button name and save it with true value in Dictionary
        self.key_states[key] = True

    def on_key_release(self,key):
        self.key_states[key] = False

    def up(self):
        self.Player.player.forward(5)       #move forward if the player want to move up

    def down(self):
        self.Player.player.backward(5)        #move backward if the player want to move down

    def move(self):
        # Player 1 controls
        if self.id==1:
            if self.key_states.get("UP"):
                self.up()
            if self.key_states.get("DOWN"):
                self.down()

        # Player 2 controls
        else:
            if self.key_states.get("W"):
                self.up()
            if self.key_states.get("S"):
                self.down()
    def take_input(self):
        if(self.id==1):
            #take input from the player
            turtle.onkeypress(lambda:self.on_key_press('UP'),'Up')
            turtle.onkeypress(lambda:self.on_key_press('DOWN'), 'Down')
            turtle.onkeyrelease(lambda: self.on_key_release('UP'), 'Up')
            turtle.onkeyrelease(lambda:self.on_key_release('DOWN'), 'Down')
        else:

            turtle.onkeypress(lambda:self.on_key_press('W'), 'w')
            turtle.onkeypress(lambda:self.on_key_press('S'), 's')
            turtle.onkeyrelease(lambda:self.on_key_release('W'), 'w')
            turtle.onkeyrelease(lambda:self.on_key_release('S'), 's')

class Ball:
    def __init__(self,ball):
        self.ball=ball
        self.x=1            #this x will be even if the ball move to the left if the ball move to the right will be odd, also i use it to make a calculation make the ball faster
    #this fun make the ball bounce if it heats a wall and also pick a random bounce angel to make the game unexpected
    def move(self):
        if self.x%2==1:                                     #
            if self.ball.player.ycor() >= 348:
                self.ball.player.setheading(random.randint(-60,-10))
            if self.ball.player.ycor() <= -348:
                self.ball.player.setheading(random.randint(10,60))
            self.ball.player.forward(1.5+self.x*0.2)   #this function make the ball get faster in the game

        else:
            if self.ball.player.ycor() >= 348:
                self.ball.player.setheading(random.randint(10,60))
            if self.ball.player.ycor() <= -348:
                self.ball.player.setheading(random.randint(-60,-10))
            self.ball.player.backward(1.5+self.x*0.2)


    def change_direction(self):
        self.x+=1                  # change x mean the ball will change the direction
    #check if the y coordination of the player and the ball are the same. the fun take player object as signature and will pick also random bouncing angle
    def checkYcordinate(self,Player):
        x = math.ceil(Player.player.ycor()) - math.ceil(self.ball.player.ycor())
        if abs(x) <= 70:
            self.ball.player.setheading(random.randint(-45,46))
            return True
        else:
            return False


