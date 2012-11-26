def f1(x):
    return x+1

def f2(x,y):
    return x/f1(y)

x=3
y=4

print ('The answer is: ', f2(x,y))
