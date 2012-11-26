from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
s = input ("Enter an integer")
n = input ("Enter another integer for number of turns.")
l = input ("Enter another integer for length.")
def polygon (t, n , l):
    angle = 360.0/n
    for i in range(n):
        fd(t,l)
        lt(t,angle)

polygon(bob, n ,l)#keyword arguments

