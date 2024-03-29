# -*- coding: utf-8 -*-
import pg
import re
from bottle import Bottle, route, run, debug, template, request, response, static_file

oop = Bottle()

# Funktio yhdistaa tietokantaan
def yhdista():
	f = open('.psqlpsswd.txt','r')
	a = f.read().strip()
	f.close()
	con = pg.connect(dbname='oopperatietokanta',host='localhost',user='verneri',passwd=a)
	return con

# Tämän avulla saadaan db-luokan funktiot käyttöön
def db_yhteys():
	f = open('.psqlpsswd.txt','r')
	a = f.read().strip()
	f.close()
	con = pg.DB(dbname='oopperatietokanta',host='localhost',user='verneri',passwd=a)
	return con

# Funktion on tarkoitus palauttaa sopivasta syötteestä muokattu sql:lle ymmärrettävä päivämäärä,
# joka on siis muotoa 2011-11-11. Palauttaa aina kahden mittaisen listan, 
# joka osoittaa aikavälin, joka syötetään sql:lle. Yhden mittaisesta syötteestä generoidaan aina kahden
# mittainen lista.

def jasenna_paivays(pvm_ehdokas):
	print "\n------------Tulostetta jasenna_paivays-funktiosta--------------------"
	print pvm_ehdokas
	ajankohdat = []
	for ehdokas in pvm_ehdokas:
		# Etsitään pisteellä toisistaa erotettuja päiviä, kuukausia ja vuosia.
		pvm = re.search("""
				(^[0-9]{2}$)							|	## Pelkkä vuosiluku muodossa vv
				(^(19|20)[0-9]{2}$) 						|	## Pelkkä vuosiluku muodossa vvvv
				(^(0?[1-9]|1[0-2])\.[12][0-9]{3}$) 				|	## Kuukausi ja vuosiluku muodossa ....vvvv
				(^(0?[1-9]|1[0-2])\.[0-9]{2}$)					|	## Kuukausi ja vuosiluku muodossa ....vv
				(^(0?[1-9]|[12][0-9])\.(0?[1-9]|[1][0-2])\.[12][0-9]{3}$)	|	## Kuukausi ja vuosi + 1. - 29. päivä muodossa ....vvvv
				(^(0?[1-9]|[12][0-9])\.(0?[1-9]|[1][0-2])\.[0-9]{2}$)		|	## Kuukausi ja vuosi + 1. - 29. päivä muodossa ....vv
				(^30\.(0?[13456789]|10|11|12)\.[12][0-9]{3}$)			|	## Mahdollisten kuukausien 30. päivä + kuukausi ja vuosi muodossa ....vvvv
				(^30\.(0?[13456789]|10|11|12)\.[0-9]{2}$)			|	## Mahdollisten kuukausien 30. päivä + kuukausi ja vuosi muodossa ....vv
				(^31\.(0?[13578]|10|12)\.[12][0-9]{3})				|	## Mahdollisten kuukausien 31. päivä + kuukausi ja vuosi ....vvvv
				(^31\.(0?[13578]|10|12)\.[0-9]{2})					## Mahdollisten kuukausien 31. päivä + kuukausi ja vuosi ....vv
				""", ehdokas, re.X) 
		# Etsitään ilman pisteitä syötettyjä päivämääriä.
		if pvm == None and (len(ehdokas) == 8 or len(ehdokas) == 6 or len(ehdokas) == 4):
			pvm = re.search("""
					(^(0[1-9]|1[0-2])[0-9]{2}$)				|	## Kuukausi ja vuosiluku kkvv
					(^(0[1-9]|1[0-2])(19|20)[0-9]{2}$)			|	## Kuukausi ja vuosiluku kkvvvv
					(^(0[1-9]|[12][0-9])(0[1-9]|1[0-2])[0-9]{2}$)		|	## Kuukausi ja vuosi + 1. -29. päivä: ppkkvv
					(^30(0[13456789]|10|11|12)[0-9]{2}$)			|	## Mahdollisten kuukausien 30. päivä + kuukausi ja vuosi: ppkkvv
					(^31(0[13578]|10|12)[0-9]{2}$)				|	## Mahdollisten kuukausien 31. päivä + kuukausi ja vuosi: ppkkvv
					(^(0[1-9]|[12][0-9])(0[1-9]|1[0-2])[12][0-9]{3}$)	|	## Kuukausi ja vuosi + 1. -29. päivä: ppkkvvvv
					(^30(0[13456789]|10|11|12)[12][0-9]{3}$)		|	## Mahdollisten kuukausien 30. päivä + kuukausi ja vuosi: ppkkvvvv
					(^31(0[13578]|10|12)[12][0-9]{3}$)				## Mahdollisten kuukausien 31. päivä + kuukausi ja vuosi: ppkkvvvv
					
					""", ehdokas,re.X)
		
		if pvm != None: print "\n------------Tää on juuri löydetty käsittelemätön päivämäärä.\t" + pvm.group() + '\n'

		sql_pvm = []
		# Muotoillaan päivämäärä sql:lle sopivaksi
		if pvm != None:
			# Päivämääräksi tulkittu numerosarja muutetaan stringiksi.
			apupaiva = pvm.group()
			# Täydennetään pisteellisten ja kahden mittaisten päivämäärien vuosiluvut 4:n mittaisiksi.
			if len(apupaiva) == 2:
				if int(apupaiva) >= 30:
					apupaiva = '19' + apupaiva
				else:
					apupaiva = '20' + apupaiva
			elif apupaiva[-3] == '.':
				if int(apupaiva[-2:]) > 30:
					apupaiva = apupaiva[:-2] + '19' + apupaiva[-2:]
				else:
					apupaiva = apupaiva[:-2] + '20' + apupaiva[-2:]
			
			# Käsitellään pisteettömien päivämäärien vuosiluvut neljän mittaisiksi.
			# Lisätään valmis vuosiluku ensimmäiseksi lopullisen päivämäärän luovaan listaan,
			# jos päivämäärän neljä viimeistä merkkiä ovat kaikki vuosiluvun osia (1900-luvun tai 2000-luvun):
			if apupaiva[-4:].startswith('19') or apupaiva[-4:].startswith('20'):
				sql_pvm.append(apupaiva[-4:])
				sql_pvm.append('-')
			# Jos eivät, tulkitaan, että neljänneksi ja kolmanneksi viimeiset kuuluvat kuukauteen. Vuosiluku täydennetään
			# joko 20:lla tai 19:llä riippuen siitä, onko vuosiluku < 30. Jos on valitaan 20, jos ei valitaan 19.
			elif int(apupaiva[-2:]) >= 30:
				apupaiva = apupaiva[:-2] + '19' + apupaiva[-2:]
				sql_pvm.append(apupaiva[-4:])
				sql_pvm.append('-')
			else:
				apupaiva = apupaiva[:-2] + '20' + apupaiva[-2:]
				sql_pvm.append(apupaiva[-4:])
				sql_pvm.append('-')

			# Lisätään pisteettömiin päivämääriin pisteet:
			if len(apupaiva) == 6 and '.' not in apupaiva:
				apupaiva = apupaiva[:2] +  '.' + apupaiva[2:]
			elif len(apupaiva) == 8 and '.' not in apupaiva:
				apupaiva = apupaiva[:2] + '.' + apupaiva[2:4] + '.' + apupaiva[4:]
			
			print "-----------\n apupaiva sen jalkeen, kun on tulkittu pvm_ehdokkaan 4 viimeista\nnumeroa muotoon vvvv tai kkvv\t\t" + apupaiva

			# Jos annetussa päivämääräehdokkaassa on enemmän kuin pelkkä vuosiluku:
			if len(apupaiva) > 4:
				# Etsi apupaivasta kaikki yhden ja kahden numeron mittaiset pätkät, ts. päivät ja kuukaudet
				d = re.findall("\d{1,2}" , apupaiva)
				## Vuosiluku poistetaan listasta
				d.pop()
				d.pop()
				d.reverse()
				for kkpp in d:
					if len(kkpp) == 2:
						sql_pvm.append(kkpp)
					else:
						sql_pvm.append('0' + kkpp)
					sql_pvm.append('-')
				print d 
			sql_pvm.pop(-1)

		## Varmistetaan, ettei helmikuussa ole 29:ää päivää muulloin kuin karkausvuonna
		if len(sql_pvm) == 5:
			if sql_pvm[2] == '02' and sql_pvm[4] == '29':
				if int(sql_pvm[0]) % 400 == 0:
					print sql_pvm
				elif int(sql_pvm[0]) % 100 == 0:
					sql_pvm.pop(-1)
					sql_pvm.pop(-1)
					print sql_pvm
				elif int(sql_pvm[0]) % 4 == 0:
					print sql_pvm
				else:
					sql_pvm.pop(-1)
					sql_pvm.pop(-1)
					print sql_pvm
		if len(sql_pvm) > 0:
			ajankohdat.append(sql_pvm)

	print '\t\tNää on ajankohdat'
	print len(ajankohdat)
	print ajankohdat

	if len(ajankohdat) > 0:
		#print len(ajankohdat[0])
		ajankohdat = sorted(ajankohdat)
		len_ajankohdat = len(ajankohdat)
		len_aja_nolla = len(ajankohdat[0])

		# Otetaan ajankohdista talteen aikaisin ja viimeisin
				
		ajat = [ajankohdat[0], ajankohdat[-1]]
		print str(ajat) + '          ajat'
		# Täydennetään päivämäärät, joista puuttuu kuukausi tai vuosi
		if len(ajat[0]) == 1:
			ajat[0].append('-')
			ajat[0].append('01')
			ajat[0].append('-')
			ajat[0].append('01')
		elif len(ajat[0]) == 3:
			ajat[0].append('-')
			ajat[0].append('01')

		if len(ajat[1]) == 1:
			ajat[1].append('-')
			ajat[1].append('12')
			ajat[1].append('-')
			ajat[1].append('31')
		elif len(ajat[1]) == 3:
			ajat[1].append('-')
			# Lisätään kuun viimeinen päivä
			if ajat[1][-2] == '02':
				if int(ajat[1][0]) % 400 == 0:
					ajat[1].append('29')
				elif int(ajat[1][0]) % 100 == 0:
					ajat[1].append('28')
				elif int(ajat[1][0]) % 4 == 0:
					ajat[1].append('29')
				else:
					ajat[1].append('28')
			elif ajat[1][-2] in ['01','03','05','07','08','10','12']:
				ajat[1].append('31')
			else:
				ajat[1].append('30')
			
		print len(ajankohdat)
		if len_ajankohdat == 1:
			if len_aja_nolla == 1:
				ajat[1] = ajat[0][:]
				ajat[1][-1] = '31'
				ajat[1][-3] = '12'
			if len_aja_nolla == 3:
				ajat[1] = ajat[0][:]
				if ajat[1][-3] == '02':
					if int(ajat[1][0]) % 400 == 0:
						ajat[1][-1] = '29'
					elif int(ajat[1][0]) % 100 == 0:
						ajat[1][-1] = '28'
					elif int(ajat[1][0]) % 4 == 0:
						ajat[1][-1] = '29'
					else:
						ajat[1][-1] = '28'
				elif ajat[1][-3] in ['01','03','05','07','08','10','12']:
					ajat[1][-1] = '31'
				else:
					ajat[1][-1] = '30'
				
		print ajat
		print "\n"
		palaute = []
		palaute.append(''.join(ajat[0]))
		palaute.append(''.join(ajat[1]))
		print palaute
		return palaute

	else:
		return []
		
#list = ['021997','2007','2011']
#jasenna_paivays(list)

class Lisaaja:   
	# Funktio lisaa dataa ooppera-tauluun
	def lisaa_ooppera(self,yhteys,oopnimi,saveltaja):
		lisays = "insert into ooppera values (DEFAULT,'" + oopnimi + "','" + saveltaja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('oop_id')").getresult()[0][0]
		return avain

	# Funktio lisää dataa rooli-tauluun
	def lisaa_oopperaan_rooli(self,yhteys,ooppera_id,roolinimi,aaniala,onko_esiintyja):
		lisays = "insert into rooli values (DEFAULT,'" + ooppera_id + "','" + roolinimi + "','" + aaniala + "','" + onko_esiintyja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('rool_id')").getresult()[0][0]
		return avain

	# Funktio lisää dataa oopperaesitys-tauluun
	def lisaa_esitys(self,yhteys,talo_id,ooppera_id,paivamaara,festivaali):
		lisays = "insert into oopperaesitys values (DEFAULT,'" + ooppera_id + "','" + talo_id + "','" + paivamaara + "','" + festivaali + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('es_id')").getresult()[0][0]
		return avain
	
	# Funktio lisää dataa oopperaesitys-tauluun
	def lisaa_oopperaan_esityspaiva(self,yhteys,ooppera_id,talo_id,paivamaara,festivaali):
		lisays = "insert into oopperaesitys values (DEFAULT,'" + ooppera_id + "','" + talo_id  + "','" + paivamaara + "','" + festivaali + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('esitys_id')").getresult()[0][0]
		return avain

	# Funktio lisää dataa henkilö-tauluun
	def lisaa_kantaan_henkilo(self,yhteys,etunimi,sukunimi,aaniala):
		lisays = "insert into henkilo values (DEFAULT,'" + etunimi + "','" + sukunimi + "','" + aaniala + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('henk_id')").getresult()[0][0]
		return avain
	
	# Funktio lisää dataa oopperatalo-tauluun
	def lisaa_kantaan_oopperatalo(self,yhteys,ooptalonnimi,ooptalonsijainti):
		lisays = "insert into oopperatalo values(DEFAULT,'" + ooptalonnimi + "','" + ooptalonsijainti + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval ('tal_id')").getresult()[0][0]
		return avain

	# Funktio lisää dataa ryhma-tauluun
	def lisaa_kantaan_ryhma(self,yhteys,ryhmannimi, ryhmantehtava):
		lisays = "insert into ryhma values(DEFAULT,'" + ryhmannimi + "','" + ryhmantehtava + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval ('ryhm_id')").getresult()[0][0]
		return avain

	# Funktio yhdistää tietokannassa olevan esityksen ja ryhman toisiinsa
	def yhdista_ryhma_esitys(self,yhteys,ryhma_id,esitys_id):
		lisays = "insert into ryhma_esitys_kombinaatio values('" + ryhma_id + "','" + esitys_id + "')"
		yhteys.query(lisays)
	
	# Funktio yhdistää tietokannassa olevan roolin, esityksen ja henkilön toisiinsa
	def yhdista_rooli_henkilo_esitys(self,yhteys,henkilo_id,rooli_id,esitys_id):
		lisays = "insert into rse_kombinaatio values('" + rooli_id + "','" + esitys_id + "','" + henkilo_id + "')"
		yhteys.query(lisays)

	

class Hakija:

	## Nettisivulla toistettavan taulukon eri osiin kirjattavat tietokannan sarakkeet
	ots_sar = ['paivamaara','saveltaja','oopnimi','ooptalonnimi','festivaali','ooptalonsijainti']
	ryhma_sar = ['ryhmannimi','ryhmantehtava']
	runko_sar = ['roolinimi','aaniala','etunimi','sukunimi','ammatti']

	def __init__(self,yhteys,hakukrit):
		self.hakukrit = hakukrit 	# Annetut hakukriteerit
		self.yhteys = yhteys		# Tietokantayhteys
		self.ots = []			# Hakutuloksen otsikko
		self.runko = []			# Hakutuloksen runko (esittäjät ja roolit, lavastajat, kapellimestari...)
		self.ryhma = []			# Hakutuloksen ryhmät (orkesteri, tanssiryhmät...)
		self.lopputulos = [self.ots, self.runko, self.ryhma]
		#print type(self.hakukrit)
		self.rajaus_kentta = []		# Hakukriteereistä luotu lista taulujen kentistä ja mitä niistä haetaan
		
		# Jos hakukriteereitä on ja jos ne ovat tyyppiä dictionary. Tämä suoritetaan vain, jos hakukriteerit
		# ovat peräisin tarkennetusta hausta.
		if (len(self.hakukrit) > 0):
			if type(self.hakukrit[0]) == type({}):
				for item in self.hakukrit:
					for sana in item.keys():
						if type(item[sana]) == type(None):
							item[sana] = '--'
						self.rajaus_kentta.append({sana : item.get(sana).split()})
		print str(self.rajaus_kentta) + 'jee'

	def haelopputulos(self):
		return self.lopputulos

	def muotoile_tulos(self,hakutulos):
		
		#Litistetään listan alilistat yhteen listaan.
		#hakutulos = [s for sanatulos in tuloslista for s in sanatulos]
		#print hakutulos
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
		hakutulos = [s for tulos in tulokset for s in tulos]
		self.muotoile_tulos(hakutulos)
	
	# Funktio luo tarkennetun haun select-osan

	def luo_select_osa(self):
		haunalku = ['SELECT ']
		for i in range(len(self.rajaus_kentta)):
			haunalku.append(''.join(self.rajaus_kentta[i].keys()))
			haunalku.append(',')
		
		print 5 * '\n' + '-------Tulostetta luo_select_osa-funktiosta------------------------------------------------'
		print str(haunalku)	
		if 'aaniala' not in haunalku and 'roolinimi' not in haunalku and 'esiintyja' in haunalku:
			haunalku.remove('esiintyja')
			haunalku.pop(-1)
			for rajaus in self.rajaus_kentta:
				if ''.join(rajaus.keys()) == 'esiintyja':
					self.rajaus_kentta.remove(rajaus)

		if haunalku[-1] == ',':
			haunalku.pop(-1)
		print str(haunalku)
		print '-------------------------------------------------------'
		return '\n\t' + ''.join(haunalku) + '\n'

	# Tämä funktio luo tarkennettuun hakuun from-osan eli luettelee taulu ja joinit.

	def luo_from_osa(self):
		print 5 * '\n' + '--------------------Tulostetta luo_from_osa-funktiosta--------------------'
		## Luodaan mahdolliset tauluyhdistelmät:
		print 'rajauskentta__________________________________'
		print self.rajaus_kentta
		tarv_taulut = []
		for y in self.rajaus_kentta:
			for x in y.keys():
				if x == 'oopnimi' or x == 'saveltaja':
					if 'ooppera' not in tarv_taulut:
						tarv_taulut.append('ooppera')
				if x == 'roolinimi' or x == 'aaniala':
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
		print tarv_taulut
		if ('rooli' in tarv_taulut and 'oopperaesitys' in tarv_taulut):
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')
		elif ('rooli' in tarv_taulut and 'oopperatalo' in tarv_taulut):
			if 'rse_kombinaatio' not in tarv_taulut:
				tarv_taulut.append('rse_kombinaatio')
			if 'oopperaesitys' not in tarv_taulut:
				tarv_taulut.append('oopperaesitys')

		if ('ooppera' in tarv_taulut and 'oopperatalo' in tarv_taulut):
			if 'oopperaesitys' not in tarv_taulut:
				tarv_taulut.append('oopperaesitys')

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

		print tarv_taulut
		print 'tarv taululut valmis__________________________________________________________'


		## Taulujen oikea järjestys kyselyjä varten:

		jarjestys = ['ooppera','rooli','oopperaesitys','rse_kombinaatio','henkilo','oopperatalo','ryhma_esitys_kombinaatio','ryhma']
		
		# Järjestetään taulut

		kyselytaulut = []

		for taulu in jarjestys:
			if taulu in tarv_taulut:
				kyselytaulut.append(taulu)

		print; print; print

		print kyselytaulut
		print '---------------------------------'
		# Luodaan sql-kyselyn from-osa. Avuksi tarvitaan PyGreSql-lisäosan db-luokkaa.
		yht = db_yhteys()
		taalta = []
		def liita_ryhma():
			taalta.append('\n\tinner join ryhma_esitys_kombinaatio as ryhes ON \n\t\t(ryhes.esitys_id = oopperaesitys.esitys_id) ' +
					'\n\tinner join ryhma ON \n\t\t(ryhes.ryhma_id = ryhma.ryhma_id)'
					)

		for i in range(len(kyselytaulut)):
			if i == 0:
				taalta.append('\tfrom ' + kyselytaulut[i] + ' ')
			else:
				if kyselytaulut[i] == 'rooli':
					taalta.append('\n\tinner join rooli ON (ooppera.ooppera_id = rooli.ooppera_id) ')
				elif kyselytaulut[i] == 'oopperaesitys':
					if 'rooli' not in kyselytaulut:
						taalta.append('\n\tinner join oopperaesitys ON \n\t\t(ooppera.ooppera_id = oopperaesitys.ooppera_id) ')
				elif kyselytaulut[i] == 'rse_kombinaatio':
					if 'oopperaesitys' in kyselytaulut and 'rooli' in kyselytaulut:
						taalta.append('\n\tinner join rse_kombinaatio ON \n\t\t(rooli.rooli_id = rse_kombinaatio.rooli_id) ')
						taalta.append('\n\tinner join oopperaesitys  ON \n\t\t(oopperaesitys.esitys_id = rse_kombinaatio.esitys_id)' )
					elif 'oopperaesitys' in kyselytaulut:
						taalta.append('\n\tinner join rse_kombinaatio ON \n\t\t(oopperaesitys.esitys_id = rse_kombinaatio.esitys_id) ')
					elif 'rooli' in kyselytaulut:
						taalta.append('\n\tinner join rse_kombinaatio ON \n\t\t(rooli.rooli_id = rse_kombinaatio.rooli_id)')
				elif kyselytaulut[i] == 'henkilo':
					taalta.append('\n\tinner join henkilo ON \n\t\t(henkilo.henkilo_id = rse_kombinaatio.henkilo_id )')
				elif kyselytaulut[i] == 'oopperatalo':
					taalta.append('\n\tinner join oopperatalo ON \n\t\t(oopperatalo.talo_id = oopperaesitys.talo_id) ')
				elif kyselytaulut[i] == 'ryhma_esitys_kombinaatio':
					liita_ryhma()
					break
										
		print '_____________________________________________________________________________________________'
		return '\n' + ''.join(taalta) + '\n'

	# Tämä funktio muokkaa päivämääriä sisältävästä listasta sql-kyselylle sopivan aikavälin. Aikaväli palautetaan 2:n mittaisena taulukkona
	# pienemmästä yhtäsuureen tai suurempaan.
	def kasittele_aikavali(paivaykset):
		aikavali = []
		for paivays in paivaykset:
			print

	def luo_where_osa(self):
		print 5 * '\n' + '-------------------Tulostetta luo_where_osa-funktiosta----------------'
		
		# Lista Dictionary-tyypin olioita.
		valiaik = []
		loppuosa = ['', '\n\tWHERE']
		for item in self.rajaus_kentta:
			if ''.join(item.get(''.join(item.keys()))) != '--':
				print self.rajaus_kentta
				if ''.join(item.keys()) != 'paivamaara': 
					valiaik.append(item)
				## Hoidetaan mahdolliset useammat päivämäärät nousevaan suuruunjärjestykseen
				else: # ''.join(item.keys()) == 'paivamaara':
					# Tässä vaiheessa tiedetään, että avain on 'paivamaara'. Otetaan syötettyjen päivämäärien lista talteen 
					# irralliseen listaan.
					temp = item.get('paivamaara') 
					# Vaihdetaan Dictionaryssä 'paivamaara'n valueksi jasenna_paivays-funktiolla käsitelty temp. 
					# 'paivamaara'n valuen pitäisi nyt olla 2-alkioinen lista.
					item['paivamaara'] = jasenna_paivays(temp)
					if item['paivamaara'] != []:
						valiaik.append(item)


		print 'rajaus_kentta:\n' + str(self.rajaus_kentta)
		print 'valiaik\n' + str(valiaik)

		if len(valiaik) > 0:
			## Käydään jokainen kenttä-hakuehto-yhdistelmä läpi.
			for i in range(len(valiaik)):

				## Hakuavaimelle helpommin ymmärrettävä muoto. avain-muuttujan arvo
				## on hakutaulun kenttä, jolle ehtoja asetetaan:
				avain = ''.join(valiaik[i].keys())


				## Hakuhedoille helpommin ymmärrettävä muoto. Ehdot-muuttujan arvo on lista
				## kentästä 'avain' haettavia merkkijonoja:
				ehdot = valiaik[i].get(''.join(valiaik[i].keys()))
				
				print '----------------avain ja ehdot-------------'
				print avain, ehdot
				print '---------------end------------------'

				for j in range(len(ehdot)):
					## Käsitellään paivamaaran haku.
					if avain == 'paivamaara':
						if j == 1:
							continue
						if i > 0:
							loppuosa.append('\t\tAND')
						loppuosa.append('\n\t\t(')
						loppuosa.append('\n\t\t\t' + avain + " >= '" + ehdot[j] + "'\n")
						loppuosa.append('\t\tAND')
						loppuosa.append('\n\t\t\t' + avain + " <= '" + ehdot[j+1] + "'\n")
						loppuosa.append('\n\t\t)\n')
					## Käsitellään kenttä-ehto-pareista ensimmäistä:
					elif i == 0:
						if len(ehdot) == 1:
							if avain == 'esiintyja':
								loppuosa.append('\n\t\t\t' + avain + " = '" + ehdot[j] + "'\n")	
							else:
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
						elif len(ehdot) > 1:
							if j == 0:
								loppuosa.append('\n\t\t(')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
							elif 0 < j < (len(ehdot) - 1):
								loppuosa.append('\t\tOR')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
							else:
								loppuosa.append('\t\tOR')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'")
								loppuosa.append('\n\t\t)\n')
					## Käsitellään muut kenttä-ehto-parit 
					elif i > 0:
						if len(ehdot) == 1:
							if avain == 'esiintyja':
								loppuosa.append('\t\tAND')
								loppuosa.append('\n\t\t\t' + avain + " = '" + ehdot[j] + "'\n")	
								print
							else:
								loppuosa.append('\t\tAND')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
						elif len(ehdot) > 1:
							if j == 0:
								loppuosa.append('\t\tAND')
								loppuosa.append('\n\t\t(')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
							elif 0 < j < (len(ehdot) - 1):
								loppuosa.append('\t\tOR')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'\n")
							else:
								loppuosa.append('\t\tOR')
								loppuosa.append('\n\t\t\t' + avain + " like '%" + ehdot[j] + "%'")
								loppuosa.append('\n\t\t)\n')

			if loppuosa[-1] == '\t\tOR' or loppuosa[-1] == '\t\tAND':
				loppuosa.pop(-1)
			
			print loppuosa
			return ''.join(loppuosa)
		
		else: return ''

	
	def tarkhaku(self):

		## Hakulauseen alku
		haunalku = self.luo_select_osa()
		#print haunalku

		## Hakulauseen from-osa		
		from_osa = self.luo_from_osa()	
		#print from_osa

		## Luodaan kyselyn where-osa.
		where_osa = self.luo_where_osa()
		print haunalku + from_osa + where_osa

		tulos = self.yhteys.query(haunalku + from_osa + where_osa).dictresult()
		print tulos
		self.muotoile_tulos(tulos)
		return tulos

class Muokkaaja(Hakija):
	# Funktiolla voidaan muokata jonkin taulun rivejä. Palauttaa 1, jos onnistui, 0 jos ei.
	def muokkaa_taulun_rivin_kenttaa(self,yhteys,taulu,rivi_idn_nimi,rivi_id,kentta,uusi_arvo):
		muokkaus = "update %s set %s ='%s' where %s ='%s'" % (taulu,kentta,uusi_arvo,rivi_idn_nimi,rivi_id)
		yhteys.query(muokkaus)
		testi = yhteys.query("select %s from %s where %s='%s'" % (kentta,taulu,rivi_idn_nimi,rivi_id)).getresult()
		if len(testi) == 0:
			return 0
		elif testi[0][0] == uusi_arvo:
			return 1
		else:
			return 0


# Tämän funktion avulla lisätään tietokantaan uusi ooppera.

@oop.route('/lisaa_ooppera', method='GET')
def lisaa_kantaan_ooppera():
	if request.GET.get('save','').strip():
		ooppera = request.GET.get('oopnimi','').strip()
		print ooppera
		saveltaja = request.GET.get('saveltaja','').strip()
        	yhteys = yhdista()
		lis = Lisaaja()
		if ooppera != '':
			oop_avain = str(lis.lisaa_ooppera(yhteys,ooppera,saveltaja))
		else:
			oop_avain = request.GET.get('ooppera_id','')
		
		# Lisätää roolit, jos sellaisia on syötetty:
		for i in range(1,23):
			rooli = 'rooli' + str(i)
			aaniala = 'aani' + str(i)
			esiintyja = 'es' + str(i)

			r = request.GET.get(rooli,'').strip()
			a = request.GET.get(aaniala,'').strip()
			e = request.GET.get(esiintyja,'').strip()
			if e == 'on':
				e = 't'
			else:
				e = 'f'

			if r == '' and a == '':
				continue
			else:
				lis.lisaa_oopperaan_rooli(yhteys,oop_avain,r,a,e)

		yhteys.close()
		return template('tarkhaku.tpl')
	elif request.GET.get('Rooleihin','').strip():
		yhteys = yhdista()
		ooppera = request.GET.get('ooppera','').strip()
		print "Tää on ooppera" + ooppera
		haku = yhteys.query("select oopnimi,saveltaja,roolinimi,aaniala from ooppera inner join rooli on (ooppera.ooppera_id = rooli.ooppera_id) where ooppera.ooppera_id = " + ooppera).dictresult()
		print haku
		roolit = Hakija(yhteys,haku)
		roolit.muotoile_tulos(haku)
		return template('lisaa_rooleja.tpl', rivit = roolit.haelopputulos(), ooppera_id = ooppera)
	else:
		yhteys = yhdista()
		oopperat = yhteys.query("select saveltaja, oopnimi, ooppera_id from ooppera order by oopnimi").getresult()
		yhteys.close()
		return template('lisaa_ooppera.tpl', rivit = oopperat)

# Tämän funktion avulla lisätään tietokantaan henkilö.
@oop.route('/lisaa_henkiloita',method='GET')
def lisaa_kantaan_henkiloita():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		lis = Lisaaja()
		for i in range(1,23):
			etunimi = 'etunimi' + str(i)
			sukunimi = 'sukunimi' + str(i)
			ammatti = 'ammatti' + str(i)

			e = request.GET.get(etunimi,'').strip()
			s = request.GET.get(sukunimi,'').strip()
			a = request.GET.get(ammatti,'').strip()
			if e != '' and s != '' and a != '':
				lis.lisaa_kantaan_henkilo(yhteys,e,s,a)
		yhteys.close()
		return template('tarkhaku.tpl')
	else:
		yhteys = yhdista()
		henkilot = yhteys.query("select henkilo_id,sukunimi,etunimi,ammatti from henkilo order by sukunimi").getresult()
		yhteys.close()
		return template('lisaa_henkiloita.tpl', rivit = henkilot)

# Tämän funktion avulla lisätään kantaan esiintymispaikkoja
@oop.route('/lisaa_oopperataloja',method='GET')
def lisaa_kantaan_oopperatalo():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		lis = Lisaaja()
		for i in range(1,6):
			ooptalonnimi = 'ooptalonnimi' + str(i)
			ooptalonsijainti = 'ooptalonsijainti' + str(i)

			oopn = request.GET.get(ooptalonnimi,'').strip()
			oops = request.GET.get(ooptalonsijainti,'').strip()

			if oopn != '' and oops != '':
				lis.lisaa_kantaan_oopperatalo(yhteys,oopn,oops)
		yhteys.close()
		return template('tarkhaku.tpl')
	else:
		yhteys = yhdista()
		ooptalot = yhteys.query("select talo_id,ooptalonnimi,ooptalonsijainti from oopperatalo order by ooptalonnimi").getresult()
		yhteys.close
		return template('lisaa_oopperataloja.tpl', rivit=ooptalot)

# Funktion avulla liitetään esityspäivä esiintymispaikkaan ja oopperaan
@oop.route('/lisaa_espaiva',method='GET')
def liita_paikkaan_paiva_ooppera():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		lis = Lisaaja()
		paivamaara = request.GET.get('paivamaara','').strip()
		paivays = [paivamaara]
		paivays = jasenna_paivays(paivays)
		if len(paivays) == 2:
			paivays = paivays[0]
		else:
			return template('tarkhaku.tpl')
		print paivays + '3'
		festivaali = request.GET.get('festivaali','').strip()
		ooppera = request.GET.get('ooppera_id','').strip()
		if ooppera == '':
			return template('tarkhaku.tpl')
		talo_id = request.GET.get('talo_id','').strip()
		if talo_id == '':
			return template('tarkhaku.tpl')
		
		lis.lisaa_esitys(yhteys,talo_id,ooppera,paivays,festivaali)
		yhteys.close()
		return template('tarkhaku.tpl')
	else:
		yhteys = yhdista()
		talot = yhteys.query('select talo_id,ooptalonnimi,ooptalonsijainti from oopperatalo order by ooptalonnimi').getresult()
		oopperat = yhteys.query('select ooppera_id,oopnimi,saveltaja from ooppera order by oopnimi').getresult()
		return template('lisaa_espaiva.tpl', ooptalot=talot, ooplista=oopperat)


# Tämän funktion avulla lisätään kantaan esiintyjäryhmiä
@oop.route('/lisaa_ryhmia', method='GET')
def lisaa_kantaan_ryhma():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		lis = Lisaaja()
		for i in range(1,6):
			ryhmannimi = 'ryhmannimi' + str(i)
			ryhmantehtava = 'ryhmantehtava' + str(i)

			rn = request.GET.get(ryhmannimi,'').strip()
			rt = request.GET.get(ryhmantehtava,'').strip()

			if rn != '' and rt != '':
				testi = yhteys.query("select ryhmannimi,ryhmantehtava from ryhma where ryhmannimi = '%s' and ryhmantehtava = '%s'" %(rn,rt)).getresult()
				if len(testi) > 0:
					print "Täsmälleen samanniminen ryhmä löytyy jo kannasta, ja sille on myös määritelty sama tehtävä. Jätettiin lisäämättä."
					continue
				else:
					lis.lisaa_kantaan_ryhma(yhteys,rn,rt)
		yhteys.close()
		return template('tarkhaku.tpl')
	else:
		yhteys = yhdista()
		ryhmat = yhteys.query('select ryhma_id,ryhmannimi,ryhmantehtava from ryhma order by ryhmannimi').getresult()
		yhteys.close()
		return template('lisaa_ryhmia.tpl', rivit=ryhmat)

# Tämä funktio liittää yhteen esitykset, roolit sekä esiintyjät ja taustahenkilöt
@oop.route('/koosta_esitys', method='GET')
def yhdista_elementit():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		lis = Lisaaja()
		roolilkm = (int)(request.GET.get('roolilkm','').strip()) + 1
		esitys = request.GET.get('esitys_id').strip()
		for i in range(1,roolilkm):
			rooli = 'rooli_id' + str(i)
			henkilo = 'henkilo_id' + str(i)
			
			r = request.GET.get(rooli,'').strip()
			h = request.GET.get(henkilo,'').strip()

			testi = yhteys.query("select * from rse_kombinaatio where rooli_id = '%s' and esitys_id = '%s'" %(r,esitys)).getresult()
			if len(testi) > 0:
				print "Roolilla on esityksessä jo esittäjä."
				continue
			else:
				if int(h) > -1:
					lis.yhdista_rooli_henkilo_esitys(yhteys,h,r,esitys)

		for i in range(1,4):
			ryhma = 'ryhma' + str(i)
			r = request.GET.get(ryhma,'').strip()
			testi = yhteys.query("select * from ryhma_esitys_kombinaatio where ryhma_id = '%s' and esitys_id = '%s'" %(r,esitys)).getresult()
			if len(testi) > 0:
				print "Ryhmä on jo merkitty tämän esityksen osatekijäksi."
				continue
			else:
				if int(r) > -1:
					lis.yhdista_ryhma_esitys(yhteys,r,esitys)
		yhteys.close()

	elif request.GET.get('Koostamaan','').strip():
		yhteys = yhdista()
		esitys_id = request.GET.get('esitys_id','').strip()
		es = yhteys.query("select esitys_id,rooli_id,oopnimi,saveltaja,roolinimi,aaniala,paivamaara from ooppera inner join rooli on (ooppera.ooppera_id=rooli.ooppera_id) inner join oopperaesitys on (ooppera.ooppera_id = oopperaesitys.ooppera_id) where esitys_id = '%s'" % esitys_id).getresult()
		es_id = 0
		if len(es) > 0:
			if len(es[0]) > 0:
				es_id = es[0][0]

		henk = yhteys.query("select henkilo_id,sukunimi,etunimi,ammatti from henkilo order by sukunimi").getresult()
		ryhm = yhteys.query("select ryhma_id, ryhmannimi, ryhmantehtava from ryhma order by ryhmannimi").getresult()
		yhteys.close()
		rlkm = len(es)
		return template('koostaminen.tpl', esitys=es, roolilkm=rlkm, henkilot=henk, esi_id=es_id, ryhmat=ryhm)

	else:
		yhteys = yhdista()
		es = yhteys.query("select esitys_id,oopnimi,saveltaja,paivamaara from ooppera inner join oopperaesitys on (ooppera.ooppera_id = oopperaesitys.ooppera_id) order by oopnimi").getresult()
		yhteys.close()
		return template('valitse_koostettava.tpl', esitykset = es)


# Liitetaan oop-sovellukseen hakusivu.

@oop.route('/pikahaku',method = 'GET')
def hae_kannasta():
	if request.GET.get('save','').strip():
		hakukrit = request.GET.get('haku','').strip().split()
		yhteys = yhdista()
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
		etunimi = {'etunimi' : request.GET.get('etunimi','').strip()}
		sukunimi = {'sukunimi' : request.GET.get('sukunimi','').strip()}
		ammatti = {'ammatti' : request.GET.get('ammatti','').strip()}
		ryhn = {'ryhmannimi' : request.GET.get('ryhmannimi','').strip()}
		ryht = {'ryhmantehtava' : request.GET.get('ryhmantehtava','').strip()}
		ooptalo = {'ooptalonnimi' : request.GET.get('ooptalonnimi','').strip()}
		ooptsij = {'ooptalonsijainti' : request.GET.get('ooptalonsijainti','').strip()}
		hakukrit = []
		for kentta in (oop,sav,roolinimi,aaniala,paiva,fest,etunimi,sukunimi,ammatti,ryhn,ryht,ooptalo,ooptsij):
			if kentta.get(''.join(kentta.keys())) != '':
				hakukrit.append(kentta)
		print '-------------------hakukrit haetarkemmin funktiosta----------------------------'
		print hakukrit
		if pelkat_es == 'true':
			hakukrit.append({'esiintyja' : pelkat_es})
		
		#for kentta in hakukrit:
		#	print kentta	
		yhteys = yhdista()
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
	yhteys = yhdista()
	tulos = yhteys.query("select ooppera.ooppera_id,rooli.ooppera_id,oopnimi,saveltaja,roolinimi,aaniala,esiintyja from ooppera inner join rooli ON (ooppera.ooppera_id = rooli.ooppera_id)")
	pal = tulos.getresult()
	#print pal
	output = template('ooptaulukko',rivit=pal)
	yhteys.close()
	return output


@oop.route('/muokkaa_henkiloa',method='GET')
def muokkaaa_henkiloa():
	if request.GET.get('save','').strip():
		yhteys = yhdista()
		henkilo_id = request.GET.get('henkilo','').strip()
		etunimi = request.GET.get('etunimi','').strip()
		sukunimi = request.GET.get('sukunimi','').strip()
		ammatti = request.GET.get('ammatti','').strip()
		onnistuiko = False
		if len(etunimi) > 0:
			yhteys.query("update henkilo set etunimi = '%s' where henkilo_id = '%s'" %(etunimi,henkilo_id))
			testi = yhteys.query("select etunimi from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
			if testi[0][0] == etunimi:
				onnistuiko = True
		if len(sukunimi) > 0:
			yhteys.query("update henkilo set sukunimi = '%s' where henkilo_id = '%s'" %(sukunimi,henkilo_id))
			testi = yhteys.query("select sukunimi from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
			if testi[0][0] == sukunimi:
				onnistuiko = True
			else:
				onnistuiko = False
		if len(ammatti) > 0:
			yhteys.query("update henkilo set ammatti = '%s' where henkilo_id = '%s'" %(ammatti,henkilo_id))
			testi = yhteys.query("select ammatti from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
			if testi[0][0] == ammatti:
				onnistuiko = True
			else:
				onnistuiko = False

		return str(onnistuiko)

	elif request.GET.get('Poista','').strip():
		yhteys = yhdista()
		henkilo_id = request.GET.get('henkilo','').strip()
		etunimi = yhteys.query("select etunimi from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
		if len(etunimi) > 0:
			etunimi = etunimi[0][0]
		else:
			etunimi = ''
		sukunimi = yhteys.query("select sukunimi from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
		if len (sukunimi) > 0:
			sukunimi = sukunimi[0][0]
		else:
			sukunimi = ''
		ammatti = yhteys.query("select ammatti from henkilo where henkilo_id = '%s'" %(henkilo_id)).getresult()
		if len(ammatti) > 0:
			ammatti = ammatti[0][0]
		else:
			ammatti = ''
		arvo = "( " + etunimi + " " + sukunimi + ', ' + ammatti + ") "
		_id = 'henkilo_id'
		taulu = 'henkilo'
		return template('vahvista_poisto.tpl', _id=_id, _id_arvo=henkilo_id, taulu=taulu, arvo= arvo)

	elif request.GET.get('Vahvista','').strip():
		yhteys = yhdista()
		henk = request.GET.get('id_arvo','').strip()
		print henk
		henk = int(henk)
		yhteys.query("delete from henkilo where henkilo_id = %s" %(henk))
		testi = yhteys.query("select henkilo_id from henkilo where henkilo_id = %s" %(henk)).getresult()
		if len(testi) == 0:
			return "Poisto onnistui"
	elif request.GET.get('Peru','').strip():
		return "Peruit poiston" + template('tarkhaku.tpl')
	else:
		yhteys = yhdista()
		henkilot = yhteys.query("select henkilo_id,etunimi,sukunimi,ammatti from henkilo order by sukunimi").getresult()
		return template('muokkaa_henk.tpl',rivit=henkilot)

@oop.route('login',method='GET')
def kirjautumissivu():
	if request.GET.get('save',''):
		user = request.GET.get('username','').strip()
		passw = request.GET.get('password','').strip()
		f = open('.oopuserwords.txt','r')
		oikein = False
		for line in f:
			if user in line and passw in line:
				oikein = True
		if not oikein:
			return template('login.tpl')
		response.set_cookie("account", user, secret='prtle123456789')
		return "Tervetuloa oopperatietokantaan %s!" % user + template('pikahaku.tpl')

	else:
		return template('login.tpl')
debug(True)
run(oop,host='localhost',port=8080,reloader = True)

