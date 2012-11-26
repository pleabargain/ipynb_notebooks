print "Greetings!"

x = raw_input("Do you want to shutdown?")
time.sleep(3)


print "You entered ", x

def shut_down(x):
    if x == "Yes":
        print "Shutting down..."
    elif x == "No":
        print "Shutdown aborted!"
    else:
        print "Sorry, I didn't understand you."
        
shut_down(x)

"""or "yes" or "Y" or "y" if I use the or
statement the script will always return Shutting down
"""
