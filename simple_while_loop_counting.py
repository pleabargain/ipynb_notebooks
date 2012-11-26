'''
simple while loop
prints 1 to 9
skips 5
'''
a = 0
while a <13:
    a+=1
            
    if a ==5:
        continue #sends procedure up to beginning of while loop
    if a ==10:    
        break # break and end procedure
    print(a)
