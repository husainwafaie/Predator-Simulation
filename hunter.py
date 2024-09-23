# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2,pi
import random
from copy import copy
import model

class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,20,20,random.random()*pi*2,5)
    
    def update(self, balls):
        lst = []
        for i in copy(balls):
            if isinstance(i, Prey):
                if super().distance(i.get_location()) < 200:
                    lst.append(i)
        if len(lst) == 0:
            pass
        elif len(lst) == 1:
            t = lst[0].get_location()
            self._angle = atan2(t[1] - self._y, t[0] - self._x)
            super().move()
        else:
            d = 200
            main = ''
            for i in lst:
                if self.distance(i.get_location()) < d:
                    d = self.distance(i.get_location())
                    main = i
            t = main.get_location()
            self._angle = atan2(t[1] - self._y, t[0] - self._x)
            super().move()
            
        
        for i in copy(balls):
            if self.contains(i.get_location()) == True:
                if isinstance(i, Prey):
                    model.remove(i)
        
            
        
