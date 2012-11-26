from swampy.TurtleWorld import *
import random

world = TurtleWorld()
bob = Turtle()
s = random.randint(3,50)
print s

def polygon(t,length,s): #t, length is the parameter
    angle = 360.0/s
    for i in range(s):
        fd(t,length)
        lt(t,angle)

polygon(t=30,length=20,s)
"""# bob is the argument, key word arguments"""
"""When you call a function, the arguments (bob, length,etc) are
assigned to the parameters 20, 10"""


