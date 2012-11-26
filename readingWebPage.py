import urllib.request
with urllib.request.urlopen("http://sourceforge.net/projects/freeplane/files/freeplane%20stable/stats/timeline")as url:
    s=url.read()

print(s)

"""
url = "http://sourceforge.net/projects/freeplane/files/freeplane%20stable/stats/timeline"
#request
request = urllib.request.urlopen(url)

#handle
handle = urllib.urlopen(request)

#read
content = handle.read()

#split the text into an array
split_page = content.split("<td header=\"files_downloads_h\>", 1);
#again
split_page =split_page[1].split(",/td>", 1)

#now to print
print ("Downloads " + split_page[0])
"""
