# -*- coding: utf-8 -*-
import pg
from bottle import Bottle, route, run, debug, template, request

oop = Bottle()


# Funktio yhdistaa tietokantaan
def yhdista(tietokanta,isanta,kayttaja,salasana):
	con1 = pg.connect(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	dbcon = pg.DB(con1)
	return [con1,dbcon]
    
# Yhdistetään tietokantaan. Toistaiseksi näin. Lopulliseen versioon täytyy keksiä jotain hienoa.

yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')[0]
dbyht = yhdista('oopperatietokanta','localhost','verneri','kissa')[1]

# Funktio lisaa dataa ooppera-tauluun
def lisaa_ooppera(yhteys,oopnimi,saveltaja):
	lisays = "insert into ooppera values (DEFAULT,'" + oopnimi + "','" + saveltaja + "')"
	yhteys.query(lisays)
	avain = yhteys.query("select currval('oop_id')").getresult()[0][0]
	return avain

def lisaa_oopperaan_rooli(yhteys,ooppera_id,roolinimi,aaniala,onko_esiintyja):
	lisays = "insert into rooli values (DEFAULT,'" + ooppera_id + "','" + roolinimi + "','" + aaniala + "','" + onko_esiintyja + "')"
	yhteys.query(lisays)
	avain = yhteys.query("select currval('rool_id')")
	return avain

class hakija:
	# Kaikille yhteiset arvot
	## Tulosrivit
	otsikkokentat = ['paivamaara','oopnimi','saveltaja','ooptalonnimi','ryhmannimi','ryhmantehtava','festivaali']
	tuloslista = []

	def __init__(self,yhteys,hakukrit,kentat):
		self.hakukrit = hakukrit
		self.yhteys = yhteys
		# Oletus
		self.kentat = kentat
		self.taulut = {}
		
	# Metodilla muokataan hakutulos hae-funktiolle sopivaan muotoon.
	def muokkaa_lopputulos(self,tulokset):
		if len(tulokset) > 0:
			valitulos= []
			# Käsitellään jokainen 'dictionary' listasta
			for tulos in tulokset:
				# Käsitellään jokainen elementti 'dictionarysta'.
				for k,v in tulos.iteritems():
					if k not  

					
		valitulos1 = []
		for item in valitulos:
			if item not in valitulos1:
				valitulos1.append(item)
		

		return valitulos1	

	def haekaikesta(self):
		tulokset = []
		for sana in self.hakukrit:
			tulos = self.yhteys.query("""
			select oopnimi,saveltaja,paivamaara,ryhmannimi,ooptalonnimi,roolinimi,aaniala,etunimi,sukunimi
				from ooppera inner join rooli ON (ooppera.ooppera_id = rooli.ooppera_id)
					inner join rse_kombinaatio as rse ON (rooli.rooli_id = rse.rooli_id)
					inner join henkilo ON (henkilo.henkilo_id = rse.henkilo_id)
					inner join oopperaesitys as oes ON (oes.esitys_id = rse.esitys_id)
					inner join ryhma_esitys_kombinaatio as rek ON (oes.esitys_id = rek.esitys_id)
					inner join ryhma ON (ryhma.ryhma_id = rek.ryhma_id)
					inner join oopperatalo ON (oopperatalo.talo_id = oes.talo_id)
					where saveltaja LIKE '%%%s%%' OR
						oopnimi LIKE '%%%s%%' OR
						roolinimi LIKE '%%%s%%' OR
						aaniala LIKE '%%%s%%' OR
						sukunimi LIKE '%%%s%%'
					order by paivamaara
			""" % (sana, sana,sana,sana,sana)).dictresult()
			print tulos
			tulokset.append(tulos)

		lopputulos = self.muokkaa_lopputulos(tulokset)
	
		print lopputulos
		return lopputulos
		

# Alustava funktio kaiken mahdollisen tiedon lisaamiseen tietokantaan

@oop.route('/lisaa', method='GET')
def lisaa_kantaan():
	if request.GET.get('save','').strip():
		ooppera = request.GET.get('oopnimi','').strip()
		print ooppera
		saveltaja = request.GET.get('saveltaja','').strip()
		paiva = request.GET.get('esityspaiva','').strip()
		rooli1_nimi = request.GET.get('rooli1_nimi','').strip()
		onko1_esiintyja = request.GET.get('onko1_esiintyja','').strip()
		if onko1_esiintyja == 'on':
			onko1_esiintyja = 'true'
		else:
			onko1_esiintyja = 'false'
		rooli1_aaniala = request.GET.get('rooli1_aaniala','').strip()
        	#yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')[0]
		oop_avain = str(lisaa_ooppera(yhteys,ooppera,saveltaja))
		rool_avain = str(lisaa_oopperaan_rooli(yhteys,oop_avain,rooli1_nimi,rooli1_aaniala,onko1_esiintyja))
		#yhteys.close()
		return "<p>Onnistui! %s</p>" % (oop_avain)
	else:
		return template('lisaa.tpl')

# Liitetaan oop-sovellukseen hakusivu.

@oop.route('/hae',method = 'GET')
def hae_kannasta():
	if request.GET.get('save','').strip():
		haetaan = request.GET.get('haku','').strip()
		hakukrit = haetaan.split()
		print hakukrit
		# yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')[0]
		kentat = ['oopnimi','saveltaja','paivamaara','ryhmannimi','ooptalonnimi','roolinimi','aaniala','etunimi','sukunimi']
		pal = hakija(yhteys,hakukrit,kentat) 
		output = template('ooptaulukko',rivit=(pal.haekaikesta()))
		#yhteys.close
		return output
	else:
		return template('hae.tpl')


# Liitetaan oop-sovellukseen tulossivu

@oop.route('/tulossivu')
def tulossivu():
	#yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')[0]
	tulos = yhteys.query("select ooppera.ooppera_id,rooli.ooppera_id,oopnimi,saveltaja,roolinimi,aaniala,esiintyja from ooppera inner join rooli ON (ooppera.ooppera_id = rooli.ooppera_id)")
	pal = tulos.getresult()
	output = template('ooptaulukko',rivit=pal)
	#yhteys.close()
	return output



debug(True)
run(oop,host='localhost',port=8080,reloader = True)

