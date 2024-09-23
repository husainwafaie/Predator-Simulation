'''
Created on Jun 4, 2022

@author: Husain Wafaie

The special object is a predator that can kill preys from far away by shooting green laser rays at them
'''

from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2,pi
import random
from copy import copy
import model
from blackhole import Black_Hole

main = ''
state = False
class Special(Pulsator, Mobile_Simulton):
    def __init__(self,x,y):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        Black_Hole.__init__(self,x,y)
    
    def update(self, balls):
        global state
        global main
        lst = []
        for i in copy(balls):
            if isinstance(i, Prey):
                lst.append(i)
        if len(lst) == 0:
            pass
        elif len(lst) == 1:
            i = random.random()
            if i < 0.2:
                t = lst[0].get_location()
                state = True
                model.remove(lst[0])
        else:
            i = random.random()
            if i < 0.2:
                d = 500
                main = ''
                for i in lst:
                    if self.distance(i.get_location()) < d:
                        d = self.distance(i.get_location())
                        main = i
                if (type(main) != str):
                    model.remove(main)
                    state = True
        
    def display(self,canvas):
        global main
        global state
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='Purple')
        if (state == True) and (type(main) != str):
            t = main.get_location()
            self.x1 = t[0]
            self.y1 = t[1]
            self.x2 = self._x
            self.y2 = self._y
            canvas.create_line(self.x1     , self.y1,
                                    self.x2, self.y2,
                                    fill='Green')
            state = False
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
