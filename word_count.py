#!/usr/bin/env
"""does not work
I get indentation error at with open
"""
import sys
def charcount(filepath):
""" function(argument):
generic function
can call it against any file
be nice to have a GUI to navigate to directories
"""
    lines = words = chars = 0
    """don't have to declare variables ahead of time"""
    try:
        with open("/home/dennis/Desktop/scripts_etc/output.txt", 'r') as f:
            for line in f:
                lines += 1
                chars += len(line)
                wordlist = line.split( ):
                    """creating an array """
                words += len(wordlist)
                """number of words """
        return lines, words, chars
                    
                
    except Exception as c:
        print(c)
        sys.exit(1)
if __name__ == '__main__':

print (charcount("/home/dennis/Desktop/scripts_etc/output.txt"))

