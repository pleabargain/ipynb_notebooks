'''
a word search program
written by: Horst Jens
with big thanks and small mods by: Dennis Daniels
'''

# i assume you are using python2.7 to work with 3.2 here
## changes made for 3.2 compatiblity:
# replace file with open
# and wrap print with ()

#possible enhancements
#add a way for user to add input
#count the total number of finds
#replace the finds with other words
#this is a word search tool... how am I creating new value with it?
##I'm creating value in my head by increasing my knowledge

# to test this , create a file called poem.txt in the same
#folder as this python file
# make sure there are a lot of "more" in the poem.txt like
poem = """there is more to the world
than Demi Moore and Roger Mooore
It is a good Morning, but more so
a good day to every moron out there,
gimme more, more, moreofit"""


# open file as fileoobject f

f = open("poem.txt","r") # open in (r)ead mode (default)

# get a big list of all the lines in the file

lines = f.readlines()

# close the file, keep the lines list only

f.close()

# define what you are looking for, the searchstring

mysearchstring = "more" # make double or single quotes, but do not mix them

# iterate over all the lines
linenumber = 0
counter = 0
currentline = ""
for line in lines: 
    linenumber += 1
    startpos = 0
    endpos = 0
    while line[endpos:].find(mysearchstring) > 0:
        counter += 1
        # find out at what position exactly
        startpos = line[endpos:].find(mysearchstring)
        endpos += startpos + len(mysearchstring)
        print ("found '{}' in line:{} pos:{}:\n{}".format(mysearchstring, linenumber, endpos-len(mysearchstring), line))
        
    print ("end of line {}".format(linenumber))
print ("end of search")
