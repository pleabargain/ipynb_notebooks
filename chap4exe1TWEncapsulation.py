from swampy.TurtleWorld import *
import random


world = TurtleWorld()
bob = Turtle()
ray = Turtle()
rand = random.randint(0,100) # need the randint

def square (t): #t is the parameter
    for i in range(8):
        #fd(t,rand) # I get this error TypeError: 'module' object is not callable because I had not set randint
        fd(t,rand)
        fd(t)
        lt(t)

square(bob)# bob is the argument
square(ray) #
"""can't see ray move because it is on
same line"""

