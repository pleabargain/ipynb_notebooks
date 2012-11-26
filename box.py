def top_line():
	print '+' + ' - '*5 + '+'
def ends():
	print "|" + "   "*5 + "|"
def do_five_times(f):
    f()
    f()
    f()
    f()
    f()
def repeat():
    top_line()
    do_five_times(ends)
    top_line()
def box():
    do_five_times(repeat)
def boxes():
    
    do_five_times(box)
    
    
boxes()


	
	
