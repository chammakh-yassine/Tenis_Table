import turtle # turtle modul

class GameObjects:
    def __init__(self,color,x,y):    #constractor
        self.player=turtle.Turtle()    #make the turtle object
        #set up the attributes
        self.player.penup()
        self.player.speed(0)
        self.player.color(color)
        self.player.setposition(x,y)
        self.player.shape('square')
        self.player.shapesize(1)
    def Show_Player(self):     # the size of the players
        self.player.setheading(90)
        self.player.shapesize(stretch_len=8, stretch_wid=1)


