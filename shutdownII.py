def shut_down(s):
    if s.lower() == "yes" :
        print "Shutting down..."
    elif s.lower() == "no":
        print "Shutdown aborted!"
    else:
        print "Sorry, I didn't understand you."
shut_down("yes")
shut_down("no")
shut_down("?")
#shut_down("y")
