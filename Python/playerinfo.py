from bs4 import BeautifulSoup
import urllib
import MySQLdb
import DatabaseConnector
import team

def get_gsid(url):
    r = urllib.urlopen('http://www.nfl.com'+url).read()

    start= r.find("GSIS ID: ")
    #jump ahead to begining of GSID
    start+=9
    #Get 10 digit GSID
    GSID= r[start:start+10]
    return GSID

def team_data(cur):
	
	for y in range(21,len(team.teams)):
		data=[]
		tds=[]
		pteam= team.teams[y][0]
		#pteam='ATL'
		r = urllib.urlopen('http://www.nfl.com/teams/roster?team='+pteam).read()
		soup = BeautifulSoup(r, "html.parser")
		table = soup.find_all('table')
		table=table[1]
		rows = table.find_all('tr')

		for rows in rows:
			cells = rows.findAll("td")
			tds.append(cells)
			cells = [ele.text.strip() for ele in cells]
			data.append([ele for ele in cells if ele])

		for x in range(1,len(data)):
			try:
				number=int(data[x][0])
				name= data[x][1]
				profile= tds[x][1].a['href']
				gsid = get_gsid(profile)
				position= data[x][2]
				status= data[x][3]
				height= data[x][4]
				weight= int(data[x][5])
				birthdate= data[x][6]
				years_pro= int(data[x][7])
				college= data[x][8]
				#team='SF'
				#print  profile, gsid, name, position, pteam, status
				cur.execute("INSERT INTO playerinfo(profile, GSID, Name, TEAM, Pos)VALUES(%s,%s,%s,%s,%s)",(profile,gsid,name,pteam,position))
				print "Succesfully added"
			except:
				print "player not added"
        	db.commit()

if __name__ == '__main__':
    #get_gsid("kenethacker","2549981")
	
	try:
		db = MySQLdb.connect(host=DatabaseConnector.host, 
                     user= DatabaseConnector.user, 
                      passwd= DatabaseConnector.passwd,
                      db=DatabaseConnector.db)
	except:
		print "Error Connecting to Database"
	cur = db.cursor() 
	print "Sucessful"
	team_data(cur)
	db.commit()
