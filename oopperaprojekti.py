# -*- coding: utf-8 -*-
import pg
from bottle import Bottle, route, run, debug, template, request

oop = Bottle()

# Funktio yhdistaa tietokantaan
def yhdista(tietokanta,isanta,kayttaja,salasana):
	con = pg.connect(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	return con

# Tämän avulla saadaan db-luokan funktiot käyttöön
def db_yhteys(tietokanta,isanta,kayttaja,salasana):
	con = pg.DB(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	return con
class Lisaaja:   
	# Funktio lisaa dataa ooppera-tauluun
	def lisaa_ooppera(self,yhteys,oopnimi,saveltaja):
		lisays = "insert into ooppera values (DEFAULT,'" + oopnimi + "','" + saveltaja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('oop_id')").getresult()[0][0]
		return avain

	def lisaa_oopperaan_rooli(self,yhteys,ooppera_id,roolinimi,aaniala,onko_esiintyja):
		lisays = "insert into rooli values (DEFAULT,'" + ooppera_id + "','" + roolinimi + "','" + aaniala + "','" + onko_esiintyja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('rool_id')")
		return avain

class Hakija:
	## Nettisivulla toistettavan taulukon eri osiin kirjattavat tietokannan sarakkeet
	ots_sar = ['paivamaara','saveltaja','oopnimi','ooptalonnimi','festivaali','ooptalonsijainti']
	ryhma_sar = ['ryhmannimi','ryhmantehtava']
	runko_sar = ['roolinimi','aaniala','etunimi','sukunimi','ammatti']

	def __init__(self,yhteys,hakukrit):
		self.hakukrit = hakukrit
		self.yhteys = yhteys
		self.ots = []
		self.runko = []
		self.ryhma = []
		self.kentat = []
		self.lopputulos = [self.ots, self.runko, self.ryhma]

	def haelopputulos(self):
		return self.lopputulos

	def muotoile_tulos(self,tuloslista):
		
		#Litistetään listan alilistat yhteen listaan.
		hakutulos = [s for sanatulos in tuloslista for s in sanatulos]

		for tulos in hakutulos:
			# Muotoillaan näytettäville tulostaulukoille otsikko-osat tpl-tiedostolle sopivaan muotoon.
			# Otsikko-osaan sisällytetään elementit, joiden arvo on useilla riveillä sama.
			otsikko = []
			for sarake in self.ots_sar :
				if sarake in tulos.keys():
					otsikko.append(tulos.get(sarake))
		
			if otsikko not in self.ots:
				self.ots.append(otsikko)
		for x in range(len(self.ots)):
			self.runko.append([])
			self.ryhma.append([])

		for i in range(len(self.ots)):
			for tulos in hakutulos:
				#print tulos
				onkosopiva = False
				for o in self.ots[i]:
					if o in tulos.values():
						onkosopiva = True
					else:
						onkosopiva = False
						break
				if onkosopiva:
					tama_ryhma = []
					for sarake in self.ryhma_sar:
						if sarake in tulos.keys():
							tama_ryhma.append(tulos.get(sarake))
					if tama_ryhma not in self.ryhma[i]:
						self.ryhma[i].append(tama_ryhma)

					tama_runko = []
					for sarake in self.runko_sar:
						if sarake in tulos.keys():
							tama_runko.append(tulos.get(sarake))
					if tama_runko not in self.runko[i]:
						self.runko[i].append(tama_runko)
		

	def haekaikesta(self):
		tulokset = []
		#db = db_yhteys('oopperatietokanta','localhost','verneri','kissa')
		kysely = """
			select oopnimi,saveltaja,paivamaara,ryhmannimi,ryhmantehtava,ooptalonnimi,ooptalonsijainti,roolinimi,aaniala,etunimi,sukunimi,ammatti
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
						sukunimi LIKE '%%%s%%' OR
						etunimi LIKE '%%%s%%' OR
						ammatti LIKE '%%%s%%' OR 
						ryhmannimi LIKE '%%%s%%' OR 
						ryhmantehtava LIKE '%%%s%%' OR 
						ooptalonnimi LIKE '%%%s%%' OR 
						ooptalonsijainti LIKE '%%%s%%' 
			"""
		leikkaus = " INTERSECT " 

		kys = []

		for i in range(len(self.hakukrit)):
			if i < len(self.hakukrit) - 1:
				kys.append(kysely)
				kys.append(leikkaus)
			else:
				kys.append(kysely)

		loppu = ['(']
		for j in range(len(self.hakukrit)):
			if j < len(self.hakukrit) - 1:
				for z in range(11):
					loppu.append('"' + self.hakukrit[j] + '",')
			else:
				for zx in range(10):
					loppu.append('"' + self.hakukrit[j] + '",')
				loppu.append('"' + self.hakukrit[j]+ '"' + ")")

		lop = ' '.join(loppu)

		valmis = " ".join(kys)
		print valmis
		print lop
		for sana in self.hakukrit:
			tulos = self.yhteys.query(valmis % eval(lop)).dictresult()
			tulokset.append(tulos)
		self.muotoile_tulos(tulokset)
	
	def tarkhaku(self):
		tulokset = []
		tarv_taulut = []
		tarv_kentat = []
		for item in hakukrit.keys():
			if item == 'etunimisukunimi':
				tarv_kentat.append('etunimi')
				tarv_kentat.append('sukunimi')
			else:
				tarv_kentat.append(item)

		

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
        	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		lis = Lisaaja()
		oop_avain = str(lis.lisaa_ooppera(yhteys,ooppera,saveltaja))
		rool_avain = str(lis.lisaa_oopperaan_rooli(yhteys,oop_avain,rooli1_nimi,rooli1_aaniala,onko1_esiintyja))
		yhteys.close()
		return "<p>Onnistui! %s</p>" % (oop_avain)
	else:
		return template('lisaa.tpl')

# Liitetaan oop-sovellukseen hakusivu.

@oop.route('/pikahaku',method = 'GET')
def hae_kannasta():
	if request.GET.get('save','').strip():
		hakukrit = request.GET.get('haku','').strip().split()
		yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		pal = Hakija(yhteys,hakukrit) 
		pal.haekaikesta()
		output = template('tulostaulukko',rivit=pal.haelopputulos())
		yhteys.close()
		return output
	else:
		return template('pikahaku.tpl')

@oop.route('/tarkhaku', method = 'GET')
def hae_tarkemmin():
	if request.GET.get('save','').strip():
		pelkat_es = request.GET.get('pelkat_esiintyjat','').strip()
		if pelkat_es == 'on':
			pelkat_es = 'true'
		else:
			pelkat_es = 'false'
		oop  = {'oopnimi' : request.GET.get('oopnimi','').strip()}
		sav  = {'saveltaja' : request.GET.get('saveltaja','').strip()}
		roolinimi = {'roolinimi':request.GET.get('roolinimi','').strip()}
		aaniala = {'aaniala' : request.GET.get('aaniala','').strip()}
		paiva = {'paivamaara' : request.GET.get('paivamaara','').strip()}
		fest= {'festivaali' : request.GET.get('festivaali','').strip()}
		etusuk = {'etunimisukunimi' : request.GET.get('etunimisukunimi','').strip()}
		ammatti = {'ammatti' : request.GET.get('ammatti','').strip()}
		ryhn = {'ryhmannimi' : request.GET.get('ryhmannimi','').strip()}
		ryht = {'ryhmantehtava' : request.GET.get('ryhmantehtava','').strip()}
		ooptalo = {'ooptalonnimi' : request.GET.get('ooptalonnimi','').strip()}
		ooptsij = {'ooptalonsijainti' : request.GET.get('ooptalonsijainti','').strip()}
		hakukrit = []
		for kentta in (oop,sav,roolinimi,aaniala,paiva,fest,etusuk,ammatti,ryhn,ryht,ooptalo,ooptsij):
			print kentta
			if (''.join(kentta.values())) != "--" and (''.join(kentta.values())) != "":
				hakukrit.append(kentta)
		hakukrit.append({'onkoesiintyja' : pelkat_es})
		
		print hakukrit	
		yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		tark = Hakija(yhteys,hakukrit)
		tark.tarkhaku()
		output = template('tulostaulukko', rivit = tark.haelopputulos())
		yhteys.close()
		return output
	else:
		return template('tarkhaku.tpl')


# Liitetaan oop-sovellukseen tulossivu

@oop.route('/tulossivu')
def tulossivu():
	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
	tulos = yhteys.query("select ooppera.ooppera_id,rooli.ooppera_id,oopnimi,saveltaja,roolinimi,aaniala,esiintyja from ooppera inner join rooli ON (ooppera.ooppera_id = rooli.ooppera_id)")
	pal = tulos.getresult()
	print pal
	output = template('ooptaulukko',rivit=pal)
	yhteys.close()
	return output



debug(True)
run(oop,host='localhost',port=8080,reloader = True)

