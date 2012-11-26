from xml.dom import minidom

src = """
<Schedule Season="2010" Timezone="Eastern">
  <Game gameId="1" Week="1" GameDate="2010-09-09" AwayTeam="MIN" HomeTeam="NO" GameTime="8:30 PM"/>
  <Game gameId="2" Week="1" GameDate="2010-09-12" AwayTeam="MIA" HomeTeam="BUF" GameTime="1:00 PM"/>
  <Game gameId="3" Week="1" GameDate="2010-09-12" AwayTeam="DET" HomeTeam="CHI" GameTime="1:00 PM"/>
  <Game gameId="4" Week="1" GameDate="2010-09-12" AwayTeam="OAK" HomeTeam="TEN" GameTime="1:00 PM"/>
</Schedule>
"""

def test_print(dom):
    for node in dom.getElementsByTagName('Game'):
        print node.getAttribute('AwayTeam'),
        print node.getAttribute('HomeTeam'),
        print node.getAttribute('Week'),
        print node.getAttribute('gameId'),
        print node.getAttribute('GameDate'),
        print node.getAttribute('GameTime')
    print ''

dom = minidom.parseString(src)
test_print(dom)

dom = minidom.parse('data.xml')
test_print(dom)

f = open('data.xml', 'r')
dom = minidom.parse(f)
test_print(dom)
f.close()

url = 'http://api.fantasyfootballnerd.com/ffnScheduleXML.php?apiKey=1'
dom = minidom.parse(urllib2.urlopen(url))
test_print(dom)
