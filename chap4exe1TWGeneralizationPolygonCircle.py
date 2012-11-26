from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def star (t,r, length,n): #t, length is the parameter
    radius = length * n 
    for i in range(n):
        fd(t,length)
        lt(t,radius)

star(bob,length =10,n = 25, r=35)# bob is the argument, key word arguments
""" When you call a function, the arguments (bob, length,etc) are
assigned to the parameters 20, 10
"""

