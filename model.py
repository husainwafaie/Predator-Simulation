import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods
from special import Special
from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from pickle import FALSE
from copy import copy

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
balls       = set()
selected = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()
    selected    = None
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#step just one update in the simulation
def step ():
    global cycle_count
    running = False
    for i in copy(balls):
        i.update(balls)
    cycle_count += 1


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected
    selected = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selected
    if selected == 'Remove':
        i1 = x - 7
        i2 = x + 7
        i3 = y - 7
        i4 = y + 7
        for i in balls:
            b = i.get_location()
            if i1 < b[0] < i2:
                if i3 < b[1] < i4:
                    balls.remove(i)
                    break
    else:
        if selected == 'Ball':
            b = Ball(x,y)
            balls.add(b)
        elif selected == 'Floater':
            b = Floater(x,y)
            balls.add(b)
        elif selected == 'Hunter':
            b = Hunter(x,y)
            balls.add(b)
        elif selected == 'Pulsator':
            b = Pulsator(x,y)
            balls.add(b)
        elif selected == 'Black_Hole':
            b = Black_Hole(x,y)
            balls.add(b)
        elif selected == 'Special':
            b = Special(x,y)
            balls.add(b)
                        


#add simulton s to the simulation
def add(s):
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    l = set()
    for i in balls:
        if p(i) == True:
            l.add(i)
    return l


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in copy(balls):
            b.update(balls)

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
        
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
