#!/usr/bin/env python
# coding:utf-8
# https://www.youtube.com/user/TheRegRunner

import os	      

def robots():
    import mechanize    # sudo apt-get install python-mechanize
    import re	        # regular expressions  ( Text Filter )
    import sys          # to get paramstring for the filename
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)
    browser.open("http://www.magistrix.de/")
    browser.select_form(nr=1)
    browser.form["q"] = "Kraftwerk,Roboter"   
    browser.submit()     
    browser.follow_link(text="Die Roboter", nr=0)
    html = browser.response().readlines()
    ##### get lyrics #################
    start=False
    lyrics=[] 
    for i in range(0,len(html)):
       line=html[i]
       OK=False
       if '<i>' in line:    # find start of the lyrics, here it was "<i>"
           start=True
       if "class" in line:  # find end of the lyrics , here it wass "class"
           start=False
       if '<p>' in line:
           OK=True
       if '<br' in line:
           OK=True
       if OK==True:
         if start==True:
           match=re.search('>[^<>]+',line)   #  <p>Text</p>   -->   ">Text"
           if match:
             lyrics.append(match.group()[1:])
    lyrics.append('\n\n\nIch hoffe hiermit geholfen zu haben\nund verbleibe mit freundlichen GrÃ¼ssen\nund schÃ¼ss')
    #### save Lyrics to Text File ##################
    Filename = sys.argv[0]
    Filename = Filename[0:-3]+'-lyrics.txt'
    SaveFile=open(Filename,'w')
    for line in lyrics:
        SaveFile.write(line+'\n')
        #print (line)  
    SaveFile.close()
    print ('Lyrics saved to '+Filename)            
    ### espeak lyrics ###########################
    os.system('espeak -v de -p0 -s150 -a200 -f "'+Filename+'" 2> /dev/null')  

if __name__ == "__main__":
    os.system('sudo apt-get install espeak')
    os.system('sudo apt-get install python-mechanize')
    robots()
