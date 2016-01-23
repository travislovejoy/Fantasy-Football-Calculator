import urllib, json
import DatabaseConnector
import MySQLdb



def passing_stats(eid,data,week,year,cur):
	
	home= ['home','away']
	for home in home:

		pid= data[eid][home]['stats']['passing'].keys()

		for pid in pid:
			name= data[eid][home]['stats']['passing'][pid]['name']
			att=  data[eid][home]['stats']['passing'][pid]['att']
			comp= data[eid][home]['stats']['passing'][pid]['cmp']
			yds= data[eid][home]['stats']['passing'][pid]['yds']
			tds= data[eid][home]['stats']['passing'][pid]['tds']
			interceptions= data[eid][home]['stats']['passing'][pid]['ints']
			twopta= data[eid][home]['stats']['passing'][pid]['twopta']
			twoptm= data[eid][home]['stats']['passing'][pid]['twoptm']
			cur.execute("INSERT INTO passing_stats(player_id, name, att, comp, yards, td, interception, twopa, twoptm, week, year)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE att=VALUES(att), comp= VALUES(comp),yards=VALUES(yards),td=VALUES(td),interception=VALUES(interception),twopa=VALUES(twopa),twoptm=VALUES(twoptm)",(pid,name, att, comp, yds,tds,interceptions,twopta,twoptm,week,year))
			print(pid,name, att, comp, yds, tds, interceptions, twopta, twoptm)

def rushing_stats(eid,data,week,year,cur):
	home= ['home','away']
	for home in home:
		pid= data[eid][home]['stats']['rushing'].keys()

		for pid in pid:
			name= data[eid][home]['stats']['rushing'][pid]['name']
			att= data[eid][home]['stats']['rushing'][pid]['att']
			yards= data[eid][home]['stats']['rushing'][pid]['yds']
			tds= data[eid][home]['stats']['rushing'][pid]['tds']
			twopta= data[eid][home]['stats']['rushing'][pid]['twopta']
			twoptm= data[eid][home]['stats']['rushing'][pid]['twoptm']

			cur.execute("INSERT INTO rushing_stats(player_id, name, att, yards, tds, twopta, twoptm, week, year)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE att=VALUES(att) ,yards=VALUES(yards),tds=VALUES(tds),twopta=VALUES(twopta),twoptm=VALUES(twoptm)",(pid,name, att, yards,tds, twopta,twoptm,week,year))
			print(pid,name,att,yards,tds,twopta,twoptm)

def receiving_stats(eid,data,week,year,cur):

	home= ['home','away']
	for home in home:
		pid= data[eid][home]['stats']['receiving'].keys()

		for pid in pid:
			name= data[eid][home]['stats']['receiving'][pid]['name']
			rec= data[eid][home]['stats']['receiving'][pid]['rec']
			yards= data[eid][home]['stats']['receiving'][pid]['yds']
			tds= data[eid][home]['stats']['receiving'][pid]['tds']
			twopta= data[eid][home]['stats']['receiving'][pid]['twopta']
			twoptm= data[eid][home]['stats']['receiving'][pid]['twoptm']

			cur.execute("INSERT INTO receiving_stats(player_id, name, rec, yards, tds, twopta, twoptm, week, year)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE rec=VALUES(rec) ,yards=VALUES(yards),tds=VALUES(tds),twopta=VALUES(twopta),twoptm=VALUES(twoptm)",(pid,name, rec, yards,tds, twopta,twoptm,week,year))
			print(pid,name,rec,yards,tds,twopta,twoptm)

def player_stats(eid, week, year):

	try:
		db = MySQLdb.connect(host=DatabaseConnector.host, 
                     user= DatabaseConnector.user, 
                      passwd= DatabaseConnector.passwd,
                      db=DatabaseConnector.db)
	except:
		print "Error Connecting to Database"
	
	cur = db.cursor()
	#eid='2015091307'
	url = "http://www.nfl.com/liveupdate/game-center/"+eid+"/"+eid+"_gtd.json"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	#print data
	passing_stats(eid,data,week, year,cur)
	db.commit()
	rushing_stats(eid,data,week, year,cur)
	db.commit()
	receiving_stats(eid,data,week, year,cur)
	db.commit()

if __name__ == '__main__':

	player_stats('2015091307',1,2015)
