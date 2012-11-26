'''
It's a number machine...
Create a multiplication table
Could be used for creating electron counts in chemical reactions.

'''
lb=int(input("Enter lower bound num: "))
ub=int(input("Enter upper bound num: "))

print ("\nYou chose {0} as your lower bound, \
and {1} as your upper bound.".format(lb,ub))

verif = input("\nProceed? (y/n):")
response = verif.lower()

if response == 'y':
    for multiplier in range (lb,(ub +1)):
        for i in range(1,11):
            print(i,"x",multiplier,"=",i*multiplier)
else:
    print("We're done!")
