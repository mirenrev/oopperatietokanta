import pg
from bottle import Bottle, route, run, debug, template, request

oop = Bottle()

# Funktio yhdistaa tietokantaan
def yhdista(tietokanta,isanta,kayttaja,salasana):
	con1 = pg.connect(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	return con1
    

@oop.route('/lisaa', method='GET')
def lisaa_kantaan():
	if request.GET.get('save','').strip():
		ooppera = request.GET.get('oopnimi','').strip()
		print ooppera
		saveltaja = request.GET.get('saveltaja','').strip()
        	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		kysely = "insert into ooppera values (DEFAULT,'" + ooppera + "','" + saveltaja + "')"
		yhteys.query(kysely)
		return '<p>juujii</p>'
	else:
		return template('lisaa.tpl')

# Liitetaan oop-sovellukseen hakusivu

@oop.route('/tulossivu')
def tulossivu():
	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
	tulos = yhteys.query("select oopnimi,saveltaja from ooppera")
	pal = tulos.getresult()
	output = template('ooptaulukko',rivit=pal)
	yhteys.close()
	return output



debug(True)
run(oop,host='localhost',port=8080,reloader = True)

