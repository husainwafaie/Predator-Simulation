# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
import random
import math

class Ball(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,random.random()*math.pi*2,self.radius)
        
    def update(self, balls):
        super().move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill='Blue')
