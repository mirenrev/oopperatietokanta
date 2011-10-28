<html>
	<head>
		<title>Tarkennettu haku</title>		
	</head>

	<body>
		<h3 align="center">Tarkennettu haku</h3>
		<div align="center">
			<form action="tarkhaku" method="GET">
				<label>Näytä ainoastaan esiintyjät, jätä taustahenkilöt pois.</label>
				<input type="checkbox" name="pelkat_esiintyjat" checked="checked"/>
				<br/>
				<br/>
				<label>Hae oopperan nimellä.</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="oopnimi" value=" -- " />
				<br/>
				<label>Hae säveltäjän nimellä.</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="saveltaja" value=" -- " />
				<br/>
				<label>Hae roolin nimellä. (Voi olla esim. Wotan tai esim. lavastaja.)</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="roolinimi" value=" -- " />
				<br/>
				<label>Hae roolin äänialan tai taustahenkilön tehtävän mukaan.</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="aaniala" value=" -- " />
				<br/>
				<label>Hae päivämäärän mukaan (esim. 2010 tai 24.12.1999).</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="paivamaara" value=" -- " />
				<br/>
				<label>Hae festivaalin nimellä</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="festivaali" value=" -- " />
				<br/>
				<label>Hae esiintyjän tai taustahenkilön nimellä</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="etunimisukunimi" value=" -- " />
				<br/>
				<label>Hae henkilön ammatin mukaan (esim. sopraano tai valaistussuunn).</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="ammatti" value=" -- " />
				<br/>
				<label>Hae ryhman nimellä. Voi olla esim. orkesterin tai balettiryhmän nimi.</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="ryhmannimi" value=" -- " />
				<br/>
				<label>Hae ryhmän tehtävän mukaan (esim. orkesteri tai kuoro).</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="ryhmantehtava" value=" -- " />
				<br/>
				<label>Hae oopperatalon nimellä</label>
				<br/>
				<input type="text" size="40" maxlength="40" name="ooptalonnimi" value=" -- " />
				<br/>
				<label>Hae oopperatalon sijainnin mukaan</label>
				<br/> 
				<input type="text" size="40" maxlength="40" name="ooptalonsijainti" value=" -- " />
				<br/>
				<input type="submit" name="save" value="save"/>
				<br/>
			</form>
		</div>



	</body>

</html>

