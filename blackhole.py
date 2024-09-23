# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from copy import copy
import model

#dead = set()
class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def update(self, balls):
        #global dead
        dead = []
        for i in copy(balls):
            if self.contains(i.get_location()) == True:
                if not isinstance(i, Black_Hole):
                    model.remove(i)
                    dead.append(i)
        return dead
        
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='Black')
        
    def contains(self,b):
        if (self._x - self.radius) < b[0] < (self._x + self.radius):
            if (self._y - self.radius) < b[1] < (self._y + self.radius):
                return True
        return False