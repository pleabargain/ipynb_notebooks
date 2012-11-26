import math

f=open("/home/dennis/Desktop/c.txt", "a")# "a" means "append."
for x in range(1,50):#a little number machine
    print((x**2,x/math.pi), file=f)
f.close()
