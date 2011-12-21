<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3 align="center">Lisää tietokantaan ooppera ja rooleja</h3>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="60%" bgcolor="#dddddd" align="center">
					<h6>Tietokannassa jo olevat oopperat</h6>
					<table border="4" width="100%">
					%for item in rivit:
						<tr>
							<td>{{item[1]}}</td>
							<td>{{item[0]}}</td>
						</tr>
					%end
					</table>
				</td>
				<td width="40%" bgcolor="#cccccc" height="100%" align="center">
					<form action="/lisaa_ooppera" method="GET">
						<label for="ooppera_id"><h6>Valitse olemassa oleva ooppera tästä.<br />Siirry lisäämään rooleja.</h6></label>	
						<select name="ooppera" id="ooppera_id" accesskey="">
							<option value="-1" selected="selected">Valitse:</option>	
							%for item in rivit:	
								<option value="{{item[2]}}">{{item[1]}}:     {{item[0]}}</option>
							%end	
						</select>
						<input type="submit" name="Rooleihin" value="Rooleihin" />
						<hr />
					</form>
					<h6>Lisää tähän uusi ooppera ja siihen roolit ja taustahenkilöt.</h6>
					<form action="/lisaa_ooppera" method="GET">
						<label style="font:caption" for = "oopnimi">Oopperan nimi:</label>
						<br />
						<input type = "text" size="40" maxlength="40" name="oopnimi" value = ""/>
						<br/>
						<label style="font:caption" for"saveltaja">Säveltäjä:</label>
						<br />
						<input type = "text" size = "40" maxlength ="40" name = "saveltaja" value = ""/>
						<br/>
						<hr />
						<label style="font:caption" for="rooli1">Roolin nimi tai muu tehtävä:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli1" value = ""/>
						<br/>
						<label style="font:caption" for="aani1">Roolin ääniala tai tehtävän nimike:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani1" value = ""/>
						<br/>
						<label style="font:caption" for="es1">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" value="on" name="es1" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli2">Roolin nimi tai muu tehtävä:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli2" value = ""/>
						<br/>
						<label style="font:caption" for="aani2">Roolin ääniala tai tehtävän nimike:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani2" value = ""/>
						<br/>
						<label style="font:caption" for"es2">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es2" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli3">Roolin nimi tai muu tehtävä:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli3" value = ""/>
						<br/>
						<label style="font:caption" for="aani3">Roolin ääniala tai tehtävän nimike:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani3" value = ""/>
						<br/>
						<label style="font:caption" for="es3">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es3" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli4">Roolin nimi tai muu tehtävä:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli4" value = ""/>
						<br/>
						<label style="font:caption" for="aani4">Roolin ääniala tai tehtävän nimike:</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani4" value = ""/>
						<br/>
						<label style="font:caption" for"es4">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es4" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli5">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli5" value = ""/>
						<br/>
						<label style="font:caption" for="aani5">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani5" value = ""/>
						<br/>
						<label style="font:caption" for"es5">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es5" />
						<br/>
						<hr />

						<label style="font:caption" for="rooli6">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli6" value = ""/>
						<br/>
						<label style="font:caption" for="aani6">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani6" value = ""/>
						<br/>
						<label style="font:caption" for"es6">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es6" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli7">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli7" value = ""/>
						<br/>
						<label style="font:caption" for="aani7">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani7" value = ""/>
						<br/>
						<label style="font:caption" for"es7">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es7" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli8">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli8" value = ""/>
						<br/>
						<label style="font:caption" for="aani8">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani8" value = ""/>
						<br/>
						<label style="font:caption" for"es5">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es8" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli9">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli9" value = ""/>
						<br/>
						<label style="font:caption" for="aani9">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani9" value = ""/>
						<br/>
						<label style="font:caption" for"es9">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es9" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli10">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli10" value = ""/>
						<br/>
						<label style="font:caption" for="aani10">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani10" value = ""/>
						<br/>
						<label style="font:caption" for"es10">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es10" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli11">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli11" value = ""/>
						<br/>
						<label style="font:caption" for="aani11">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani11" value = ""/>
						<br/>
						<label style="font:caption" for"es11">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es11" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli12">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli12" value = ""/>
						<br/>
						<label style="font:caption" for="aani12">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani12" value = ""/>
						<br/>
						<label style="font:caption" for"es5">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es12" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli13">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli13" value = ""/>
						<br/>
						<label style="font:caption" for="aani13">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani13" value = ""/>
						<br/>
						<label style="font:caption" for"es13">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es13" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli14">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli14" value = ""/>
						<br/>
						<label style="font:caption" for="aani14">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani14" value = ""/>
						<br/>
						<label style="font:caption" for"es14">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es14" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli15">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli15" value = ""/>
						<br/>
						<label style="font:caption" for="aani15">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani15" value = ""/>
						<br/>
						<label style="font:caption" for"es15">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es15" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli16">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli16" value = ""/>
						<br/>
						<label style="font:caption" for="aani16">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani16" value = ""/>
						<br/>
						<label style="font:caption" for"es16">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es16" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli17">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli17" value = ""/>
						<br/>
						<label style="font:caption" for="aani17">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani17" value = ""/>
						<br/>
						<label style="font:caption" for"es17">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es17" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli18">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli18" value = ""/>
						<br/>
						<label style="font:caption" for="aani18">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani18" value = ""/>
						<br/>
						<label style="font:caption" for"es18">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es18" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli19">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli19" value = ""/>
						<br/>
						<label style="font:caption" for="aani19">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani19" value = ""/>
						<br/>
						<label style="font:caption" for"es19">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es19" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli20">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli20" value = ""/>
						<br/>
						<label style="font:caption" for="aani20">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani20" value = ""/>
						<br/>
						<label style="font:caption" for"es20">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es20" />
						<br/>
						<hr />
						<label style="font:caption" for="rooli21">Roolin nimi tai muu tehtävä</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "rooli21" value = ""/>
						<br/>
						<label style="font:caption" for="aani21">Roolin ääniala tai tehtävän nimike</label>
						<br/>
						<input type = "text" size = "40" maxlength ="40" name = "aani21" value = ""/>
						<br/>
						<label style="font:caption" for"es21">Onko kyseessä esiintyjä?</label>
						<input type="checkbox" checked="checked" name="es21" />
						<br/>
						<hr />
						<input type="submit" name = "save" value = "save"/>
					</form>
				</td>
			</tr>	
		</table>
	</body>
</html>
