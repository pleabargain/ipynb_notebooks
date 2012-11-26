my_list = ['fizz', 'another_word', 'fizz', 'spam', 'fizz']

def fizzCount():
    count = 0
    for word in my_list:
        if word == 'fizz':
            count = count + 1
            print(count)
    else:
        False

print (fizzCount())
