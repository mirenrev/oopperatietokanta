# -*- coding: utf-8 -*-
import pg
import re
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

# Funktion on tarkoitus palauttaa sopivasta syötteestä muokattu sql:lle ymmärrettävä päivämäärä,
# joka on siis muotoa 2011-11-11. Muutettava: otetaan syöte listana. Palautetaan aina kahden mittainen lista, 
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
	print len(ajankohdat[0])
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
		
list = ['021997','2007','2011']
jasenna_paivays(list)

class Lisaaja:   
	# Funktio lisaa dataa ooppera-tauluun
	def lisaa_ooppera(self,yhteys,oopnimi,saveltaja):
		lisays = "insert into ooppera values (DEFAULT,'" + oopnimi + "','" + saveltaja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('oop_id')").getresult()[0][0]
		return avain

	# Funktio lisää dataa ooppera-tauluun
	def lisaa_oopperaan_rooli(self,yhteys,ooppera_id,roolinimi,aaniala,onko_esiintyja):
		lisays = "insert into rooli values (DEFAULT,'" + ooppera_id + "','" + roolinimi + "','" + aaniala + "','" + onko_esiintyja + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('rool_id')").getresult[0][0]
		return avain
	
	# Funktio lisää dataa oopperaesitys-tauluun
	def lisaa_oopperaan_esityspaiva(self,yhteys,ooppera_id,talo_id,paivamaara,festivaali):
		lisays = "insert into oopperaesitys values (DEFAULT,'" + ooppera_id + "','" + talo_id  + "','" + paivamaara + "','" + festivaali + "')"
		yhteys.query(lisays)
		avain = yhteys.query("select currval('esitys_id')").getresult[0][0]
		return avain

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
		yht = db_yhteys('oopperatietokanta','localhost','verneri','kissa')
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
				valiaik.append(item)
				## Hoidetaan mahdolliset useammat päivämäärät nousevaan suuruunjärjestykseen
				if ''.join(item.keys()) == 'paivamaara':
					# Tässä vaiheessa tiedetään, että avain on 'paivamaara'. Otetaan syötettyjen päivämäärien lista talteen 
					# irralliseen listaan.
					temp = item.get('paivamaara') 
					# Vaihdetaan Dictionaryssä 'paivamaara'n valueksi jasenna_paivays-funktiolla käsitelty temp. 
					# 'paivamaara'n valuen pitäisi nyt olla 2-alkioinen lista.
					item['paivamaara'] = jasenna_paivays(temp)

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



# Alustava funktio kaiken mahdollisen tiedon lisaamiseen tietokantaan

@oop.route('/lisaa', method='GET')
		
def lisaa_kantaan_ooppera():
	if request.GET.get('save','').strip():
		ooppera = request.GET.get('oopnimi','').strip()
		print ooppera
		saveltaja = request.GET.get('saveltaja','').strip()
        	yhteys = yhdista('oopperatietokanta','localhost','verneri','kissa')
		lis = Lisaaja()
		oop_avain = str(lis.lisaa_ooppera(yhteys,ooppera,saveltaja))
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
	#print pal
	output = template('ooptaulukko',rivit=pal)
	yhteys.close()
	return output



debug(True)
run(oop,host='localhost',port=8080,reloader = True)

