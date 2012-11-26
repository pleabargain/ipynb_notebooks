from elementtree import ElementTree
root= ElementTree.parse('/home/dennis/test.odp_FILES/content.xml').getroot()
print root
#does not work
