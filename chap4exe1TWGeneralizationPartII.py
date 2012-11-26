from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def square (t,length): #t, length is the parameter
    for i in range(4):
        fd(t,length)
        lt(t)

square(bob,80)# bob is the argument

