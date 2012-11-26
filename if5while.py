'''
demonstrating while loops
'''
while True: # careful of infinite loops
    s = input ('Enter a string of at least for chars or q to quit: ')
    if s == 'q':
        break
    if len(s) < 4:
        print (s)
        print("Value is too small.")
        continue
    
    print (s)
    print("The str was of sufficient length.")
    

    raise SystemExit
    
