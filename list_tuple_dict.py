val1 = input("Enter str element 1/3: ")
val2 = int(input("Enter int element 2/3: "))
val3 = float(input("Enter flt element 3/3: "))

lst = [val1,val2,val3]
tpl = (val1,val2,val3)
dict = {"First element: ":val1,"Second element :":val2,"Third element :":val3}

print ("\n")
print ("Here is your list: ", lst)
print ("Here is your tuple: ", tpl)
print ("Here is your dictionary: ", dict)

print ("\n")
val4 =str(input("Add a new str element: "))
lst.append(val4)
print("Here is your new list: ",lst)
