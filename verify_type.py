"""
def distance_from_zero(x):
    if type(x) == str:
        print "This isn't an integer or a float!"
    elif type(x) == int:
        print abs(x), + "this in int"
    elif type(x) == float:
        print abs(x), + "this is a float"
    else:
        return "Blah"
distance_from_zero(34.3)
"""

x=raw_input("Enter a number:")
def check_type(x):
    if type(x)=='int':
        return abs(x)
    elif type(x)=='float':
        return abs(x)
    else:
        return "This isn't an integer or a float!"
    

