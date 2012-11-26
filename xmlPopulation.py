from xml.dom import minidom

xml = minidom.parse("/home/dennis/test.odp_FILES/content.xml")

kml = xmldoc.getElementsByTagName("office:document-content")[0]

body = office:document-content.getElementsByTagName("office:body")[0]

presentation = office:presentation.getElementsByTagName("office:presentation")[0]

