"""
does not work as the api has been closed
"""

import urllib2 as net
import xml.dom.minidom as xDom

class weather:
    api = "http://www.google.com/ig/api?weather="
    wData = None
    def __init__ (self, location):
        self.api = self.api + location
        self.wData = net.urlopen(self.api).read()
    def showXML(self):
        print self.wData
    def parse(self):
        xData = xDom.parseString(self.wData)
        current_conditions = xData.getElementsByTagName('current_conditions')
        temp_f = current_conditions[0].childNodes[1].getAttribute('data')
        print temp_f



w= weather("13433")
w.parse()
        
