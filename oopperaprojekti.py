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
	
	def jasenna_paivays(self,paivamaara):
		return 1


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
		kysytyt_taulut = []
		tarv_taulut = []
		rajaus_kentat = []
		for item in self.hakukrit:
			for sana in item.keys():
				if sana == 'etunimisukunimi':
					rajaus_kentat.append({'etunimi' : item.get(sana).split()})
					rajaus_kentat.append({'sukunimi' : item.get(sana).split()})
				else:
					rajaus_kentat.append({sana : item.get(sana).split()})
				
		print rajaus_kentat

		## Hakulauseen alku

		haunalku = ['SELECT ']
		for i in range(len(rajaus_kentat)):
			if i < (len(rajaus_kentat) - 1):
				haunalku.append(''.join(rajaus_kentat[i].keys()))
				haunalku.append(',')
			else:
				haunalku.append(''.join(rajaus_kentat[i].keys()))

		print ''.join(haunalku)
		
		## Luodaan mahdolliset tauluyhdistelmät:

		for y in rajaus_kentat:
			for x in y.keys():
				if x == 'oopnimi' or x == 'saveltaja':
					if 'ooppera' not in tarv_taulut:
						tarv_taulut.append('ooppera')
				if x == 'roolinimi' or x == 'onkoesiintyja' or x == 'aaniala':
					if 'rooli' not in tarv_taulut:
						tarv_taulut.append('rooli')
				if x == 'paivamaara' or x == 'festivaali':
					if 'oopperaesitys' not in tarv_taulut:
						tarv_taulut.append('oopperaesitys')
				if x == 'ooptalonnimi' or x == 'ooptalonsijainti':
					if 'oopperatalo' not in tarv_taulut:
						tarv_taulut.append('oopperatalo')
				if x == 'etunimi' or x == 'sukunimi' or x == 'ammatti':
					if 'henkilo' not in tarv_taulut:
						tarv_taulut.append('henkilo')
				if x == 'ryhmannimi' or x == 'ryhmantehtava':
					if 'ryhma' not in tarv_taulut:
						tarv_taulut.append('ryhma')
		if ('rooli' in tarv_taulut and 'oopperaesitys' in tarv_taulut):
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')

		if 'ooppera' in tarv_taulut and 'oopperatalo' in tarv_taulut:
			if 'ooppera_esitys' not in tarv_taulut:
				tarv_taulut.append('ooppera_esitys')

		if ('rooli' in tarv_taulut or 'oopperaesitys' in tarv_taulut) and 'henkilo' in tarv_taulut:
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')
		elif ('ooppera' in tarv_taulut or 'oopperatalo' in tarv_taulut) and 'henkilo' in tarv_taulut:
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')
			if 'oopperaesitys' not in tarv_taulut:
				tarv_taulut.append('oopperaesitys')

		if 'oopperaesitys' in tarv_taulut and 'ryhma' in tarv_taulut:
			if 'ryhma_esitys_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('ryhma_esitys_kombinaatio')
		elif ('ooppera' in tarv_taulut or 'oopperatalo' in tarv_taulut) and 'ryhma' in tarv_taulut:
			if 'ryhma_esitys_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('ryhma_esitys_kombinaatio')
			if 'oopperaesitys' not in tarv_taulut:
				tarv_taulut.append('oopperaesitys')
		elif ('rooli' in tarv_taulut or 'henkilo' in tarv_taulut) and 'ryhma' in tarv_taulut:
			if 'ryhma_esitys_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('ryhma_esitys_kombinaatio')
			if 'oopperaesitys' not in tarv_taulut:
				tarv_taulut.append('oopperaesitys')
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')
			
				
			
		## Taulujen oikea järjestys kyselyjä varten:

		jarjestys = ['ooppera','rooli','oopperaesitys','rse_kombinaatio','henkilo','oopperatalo','ryhma_esitys_kombinaatio','ryhma']
		
		# Järjestetään taulut

		kyselytaulut = []

		for taulu in jarjestys:
			if taulu in tarv_taulut:
				kyselytaulut.append(taulu)

		print; print; print

		print kyselytaulut

		# Luodaan sql-kyselyn from-osa. Avuksi tarvitaan PyGreSql-lisäosan db-luokkaa.
		con = db_yhteys('oopperatietokanta','localhost','verneri','kissa')
		
		taalta = []

		for i in range(len(kyselytaulut)):
			if i == 0:
				if ((kyselytaulut[i] == 'rooli') and (kyselytaulut[i + 1] == 'oopperaesitys')):
					taalta.append('from rooli inner join rse_kombinaatio ON (rooli.rooli_id = rse_kombinaatio-rooli_id)' )
				else:
					taalta.append(
							kyselytaulut[i] + 
							' inner join ' +
							kyselytaulut[i+1] +
							' ON (') +
							kyselytaulut[i] + '.'
							con.pkey(kyselytaulut[i]) + '=' +
							kyselytaulut[i+1] + '.' +
							con.pkey(kyselytaulut[i]) + ') '
							)

							
			else:
				if ((kyselytaulut[i] == 'rooli') and (kyselytaulut[i + 1] == 'oopperaesitys')):
					taalta.append('rooli ' )
				elif kyselytaulut[i].endswith('kombinaatio'):
					taalta.append("inner join " +  
							kyselytaulut[i] + 
							" ON (" + 
							kyselytaulut[i] + "." + 
							con.pkey(kyselytaulut[i-1]) + "=" +
							kyselytaulut[i+1] + "." +
							con.pkey(kyselytaulut[i-1])+ ") ")
				else:
					taalta.append("inner join " +  
							kyselytaulut[i] + 
							" ON (" + 
							kyselytaulut[i] + "." + 
							con.pkey(kyselytaulut[i]) + "=" +
							kyselytaulut[(i)] + "." +
							con.pkey(kyselytaulut[i]) + ") ")
		taalta_osa = ''.join(taalta)
		print
		print
		print taalta_osa
		print
		print


		#if 'oopnimi' in tarv_kentat or 'saveltaja' in tarv_kentat:
		#	print

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
			if kentta.get(''.join(kentta.keys())) != '':
				hakukrit.append(kentta)

		if pelkat_es == 'true':
			hakukrit.append({'onkoesiintyja' : pelkat_es})
		
		for kentta in hakukrit:
			print kentta	
		yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		tark = Hakija(yhteys,hakukrit)
		tark.tarkhaku()
		#output = template('tulostaulukko', rivit = tark.haelopputulos())
		yhteys.close()
		#return output
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

