#! /usr/bin/env python

# Tiedosto sisaltaa oopperatietokannan sql-kyselyt

import pg,sys

# Funktio yhdistaa tietokantaan

def yhdista(tietokanta,isanta,kayttaja,salasana):
	con1 = pg.connect(dbname=tietokanta,host=isanta,user=kayttaja,passwd=salasana)
	return con1

con1 = yhdista(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

# Lue web-lomakkeelta kayttajan hakuehdot

def lue_haku_sarakkeet():
	return True


# Hae yksi tieto yhdesta taulusta

def hae_yhdesta(taulu,sarakkeet):
	hakutulos = con1.query("select %s from %s" % (sarakkeet,taulu))
	return hakutulos

def hae_yhdesta_rajaten(taulu,sarakkeet,sarake,rajaus):
	hakutulos = con1.query("select %s from %s where %s like '%%%s%%'" % (sarakkeet,taulu,sarake,rajaus))
	return hakutulos

def hae_ooppera_join_rooli(sarakkeet):
	hakutulos = con1.query("select %s from ooppera inner join rooli using ooppera_id" % (sarakkeet))

tulos = hae_yhdesta('ooppera','oopnimi,saveltaja')
print type(tulos)
print tulos
tulos = hae_yhdesta_rajaten('ooppera','oopnimi,saveltaja','saveltaja','r')
print tulos
