A = [0,1,2,3,4,5,6,7,8,9,'fizz',11,12,'fizz']

def fizzCount(A):
    count = 0
    for word in A:
        if 'fizz' in A:
            count = count + 1
            return count
            #print(count)
#fizzCount(A)
