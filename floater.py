# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,random()*math.pi*2,self.radius)
        
    def update(self, balls):
        n = (random() - 0.5)
        m = (random() - 0.5)
        if 3 < (self._speed + n) < 7:
            self._speed += n
        self._angle += m
        super().move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='Red')
    