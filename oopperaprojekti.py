# -*- coding: utf-8 -*-
import pg
from bottle import Bottle, route, run, debug, template, request

oop = Bottle()

# Funktio yhdistaa tietokantaan
def yhdista(tietokanta,isanta,kayttaja,salasana):
	con1 = pg.connect(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	return con1
    
# Funktio lisaa dataa ooppera-tauluun
def lisaa_ooppera(yhteys,oopnimi,saveltaja):
	lisays = "insert into ooppera values (DEFAULT,'" + oopnimi + "','" + saveltaja + "')"
	yhteys.query(lisays)
	avain = yhteys.query("select currval('oop_id')").getresult()[0][0]
	return avain


# Alustava funktio kaiken mahdollisen tiedon lisaamiseen tietokantaan

@oop.route('/lisaa', method='GET')
def lisaa_kantaan():
	if request.GET.get('save','').strip():
		ooppera = request.GET.get('oopnimi','').strip()
		print ooppera
		saveltaja = request.GET.get('saveltaja','').strip()
		paiva = request.GET.get('esityspaiva','').strip()
        	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		oop_avain = lisaa_ooppera(yhteys,ooppera,saveltaja)
		print oop_avain
		yhteys.close()
		return "<p>Onnistui! %s</p>" % (oop_avain)
	else:
		return template('lisaa.tpl')

# Liitetaan oop-sovellukseen hakusivu

@oop.route('/tulossivu')
def tulossivu():
	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
	tulos = yhteys.query("select ooppera_id,oopnimi,saveltaja from ooppera")
	pal = tulos.getresult()
	output = template('ooptaulukko',rivit=pal)
	yhteys.close()
	return output



debug(True)
run(oop,host='localhost',port=8080,reloader = True)

