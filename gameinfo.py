from xml.dom import minidom
from gamestats import player_stats
import urllib
import cPickle
import gamestats
final= cPickle.load(open('save.p', 'rb'))
url_str = 'http://www.nfl.com/liveupdate/scorestrip/ss.xml'
xml_str = urllib.urlopen(url_str).read()
xmldoc = minidom.parseString(xml_str)
gms = xmldoc.getElementsByTagName('gms')

year= gms[0].attributes['y'].value
week= gms[0].attributes['w'].value

gm = xmldoc.getElementsByTagName('g')
for g in gm:
	
	if g.attributes['q'].value != 'P':
		eid= g.attributes['eid'].value
		if eid not in final:
			quarter= g.attributes['q'].value
			home= g.attributes['h'].value
			away= g.attributes['v'].value
			homeScore= g.attributes['hs'].value
			visitorScore= g.attributes['vs'].value
			
			player_stats(eid,week, year)
			print(eid,quarter,home,away,homeScore,visitorScore, week, year)

			if quarter== 'F' or quarter== 'FO':
				final.append(eid)

print final
cPickle.dump(final, open('save.p', 'wb')) 
			

