"""parrot = "But what if you wanted to convert thousands of words to all-lower case? Doing it manually would take forever."
print parrot.lower()
"""

"""parrot = get_page('http://what-if.xkcd.com/')
print parrot.lower ()"""

"""
---------
Trying to import text from web pages and then convert the whole page to lower case
----------
import urllib

def get_page(url)
    opener = urllib.FancyURLopener({})
    open_page = opener.open(url)
    page = open_page.read()
    return page

print get_page("http://www.google.com")
"""
