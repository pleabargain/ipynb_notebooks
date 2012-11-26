#this works
import urllib.request
with urllib.request.urlopen("http://sourceforge.net/projects/freeplane/files/freeplane%20stable/stats/timeline")as url:
    s=url.read()

print(s)

#the with/ as construct closes the page as soon as its finished reading
