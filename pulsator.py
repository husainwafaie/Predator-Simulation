# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole): 
    radius = 10
    counter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        
    def update(self, balls):
        b = super().update(balls)
        if len(b) != 0:
            for _ in b:
                self.counter = 30
                self.radius += 0.5
                self.change_dimension(1,1)
        else:
            self.counter -= 1
            if self.counter == 0:
                self.radius -= 0.5
                self.change_dimension(1,1)
                if self.radius == 0:
                    model.remove(self)
                self.counter = 30   
        
