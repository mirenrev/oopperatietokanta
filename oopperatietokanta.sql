/*Luodaan sekvenssi 'oop_id' automaattiseen ooppera-taulun pääavaimen generoimiseen.*/

create sequence oop_id start with 0 increment by 1;

/* Luodaan ooppera-taulu */

create table ooppera (
	ooppera_id integer default nextval('oop_id') not null,
	oopnimi varchar(40) default null,
	savaltaja varchar(40) default null,
	constraint ooppera_pkey primary key (ooppera_id)
);

/* Luodaan sekvenssi rool_id' automaattiseen rooli-taulun pääavaimen generoimiseen.*/

create sequence rool_id start with 0 increment by 1;

/* Luodaan rooli-taulu*/

create table rooli (
	rooli_id integer default nextval('rool_id') not null,
	ooppera_id integer not null,
	roolinimi varchar (40) default null,
	aaniala varchar (40) default null,
	constraint rooli_pkey primary key (rooli_id)
);

/* Luodaan sekvenssi 'es_id' automaattiseen oopperaesitys-taulun pääavaimen generoimiseen.*/

create sequence es_id start with 0 increment by 1;

/*Luodaan oopperaesitys-taulu*/

create table oopperaesitys (
	esitys_id integer default nextval('es_id'),
	ooppera_id integer not null,
	talo_id integer not null,
	paivamaara date default null,
	festivaali varchar (40) default null,
	constraint oopperaesitys_pkey primary key (esitys_id)
);

/* Luodaan sekvenssi 'tal_id' automaattiseen oopperatalo-taulun pääavaimen generointiin.*/

create sequence tal_id start with 0 increment by 1;

/* Luodaan oopperatalo-taulu */

create table oopperatalo (
	talo_id integer default nextval('tal_id'),
	ooptalonnimi varchar (40) default null,
	ooptalonsijainti varcha (40) default null,
	constraint oopperatalo_pkey primary key (talo_id)
);

/* Luodaan sekvenssi henk_id henkilo-taulun pääavaimen automaattiseen generointiin. */

create sequence henk_id start with 0 increment by 1;

/* Luodaan henkilo-taulu */

create table henkilo (
	henkilo_id integer default nextval('henk_id'),
	etunimi varchar (40) default null,
	sukunimi varchar (40) default null,
	tehtava varchar (40) default null,
	constraint henkilo_pkey primary key (henkilo_id)
);

/* Luodaan sekvenssi 'ryhm_id' automaattiseen ryhma-taulun pääavaimen generoimiseen. */

create sequence ryhm_id start with 0 increment by 1;

/* Luodaan ryhma-taulu */

create table ryhma (
	ryhma_id integer default nextval ('ryhm_id'),
	ryhmannimi varchar (40) default null,
	ryhmantehtava varchar (40) default null,
	constraint ryhma_pkey primary key (ryhma_id)
);

/* Luodaan rse_kombinaatio-taulu. */

create table rse_kombinaatio (
	rooli_id integer not null,
	esitys_id integer not null,
	henkilo_id integer not null,
	constraint rse_kombinaatio_pkey primary key (rooli_id,esitys_id, henkilo_id)
);

/*Luodaan ryhma_esitys__kombinaatio-taulu*/

create table ryhma_esitys_kombinaatio (
	ryhma_id integer not null,
	esitys_id integer not null,
	constraint ryhma_esitys_kombinaatio_pkey primary key (ryhma_id, esitys_id)
);

/* Luodaan tauluille foreign key -rajoitteet */

alter table rooli add constraint rooli_fkey_ooppera_id foreign key references ooppera_id ooppera(ooppera_id);

alter table oopperaesitys add constraint oopperaesitys_fkey_ooppera_id foreign key ooppera_id references ooppera(ooppera_id);

alter table oopperaesitys add constraint oopperaesitys_fkey_talo_id foreign key talo_id references oopperatalo(talo_id);

alter table rse_kombinaatio add constraint rse_kombinaatio_fkey_rooli_id foreign key rooli_id references rooli(rooli_id);

alter table rse_kombinaatio add constraint rse_kombinaatio_fkey_esitys_id foreign key esitys_id references oopperaesitys(esitys_id);

alter table rse_kombinaatio add constraint rse_kombinaatio_fkey_henkilo_id foreign key henkilo_id references henkilo(henkilo_id);

alter table ryhma_esitys_kombinaatio add constraint ryhma_esitys_kombinaatio_fkey_ryhma_id foreign key ryhma_id references ryhma(ryhma_id);

alter table ryhma_esitys_kombinaatio add constraint ryhma_esitys_kombinaatio_fkey_esitys_id foreign key esitys_id references oopperaesitys(esitys_id);
