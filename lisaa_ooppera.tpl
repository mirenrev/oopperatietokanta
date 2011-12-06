<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<h3 align="center">Lisää tietokantaan ooppera ja rooleja</h3>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="60%" bgcolor="#dddddd" align="center">
					<h6>Tietokannassa jo olevat oopperat</h6>
					<table border="4" width="100%" height="90%">
					%for item in rivit:
						<tr>
							<td>{{item[0]}}</td>
							<td>{{item[1]}}</td>
						</tr>
					%end
					</table>
				</td>
				<td width="40%" bgcolor="#cccccc" height="100%" align="center">
					<h6>Kirjoita tähän lisättävän oopperan tiedot</h6>
					<form action="/lisaa_ooppera" method="GET">
						<label style="font:caption" for"oopnimi">Oopperan nimi:</label>
						<br />
						<input type = "text" size="40" maxlength="40" name="oopnimi" value = ""/>
						<br/>
						<label style="font:caption" for"saveltaja">Säveltäjä:</label>
						<br />
						<input type = "text" size = "40" maxlength ="40" name = "saveltaja" value = ""/>
						<br/>
						<hr />
						<label for="ooppera_id"><h6>...tai valitse olemassa oleva ooppera tästä.</h6></label>	
						<select id="ooppera_id" accesskey="">
							<option value="-1" selected="selected">Valitse:</option>	
							%for item in rivit:	
								<option value="{{item[2]}}">{{item[1]}}:     {{item[0]}}</option>
							%end	
						</select>
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
						<input type="checkbox" checked="checked" name="es1" />
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
						<input type="submit" name = "save" value = "save"/>
					</form>
				</td>
			</tr>	
		</table>
	</body>
</html>
