<html>
	<head>
	</head>

	<body>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="60%" bgcolor="#dddddd" align="center">	
					<h6>Olemassa olevat roolit oopperassa</h6>
					%for i in range(len(rivit[0])):
					 <table border="10" width = "400">
						 <th>Ooppera</th>
						 %for item in rivit[0][i]:
							 <tr>
								 <td align ="center">{{item}} </td>
							 </tr>
						 %end
					 
						 <th>Toteuttajat</th>
						 %for jtem in rivit[1][i]:
							 <tr>
							 %for x in jtem:
									 <td align="center">{{x}}</td>
							 %end
							 </tr>
						 %end
						 <th>Ryhmät</th>
						 %for ktem in rivit[2][i]:
							 <tr>
							 %for y in ktem:
								 <td align="center">{{y}}</td>
							 %end
							 </tr>
						 %end
					</table>
					 %end
				</td>
				<td widtht="40%" bgcolor="#cccccc" heigth="100%" align="center">
					<h6>Lisää vasemmassa sarakkeessa näkyvään ooppeeraan rooleja.</h3>
					<form action="lisaa_ooppera" method="GET">
						<input type="hidden" name="ooppera_id" value="{{ooppera_id}}" />
						<input type="submit" name="save" value="save" />
						<br />
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
                                                <label style="font:caption" for="es2">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es2" />
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
                                                <input type="checkbox" checked="checked" value="on" name="es3" />
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
                                                <label style="font:caption" for="es4">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es4" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli5">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli5" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani5">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani5" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es5">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es5" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli6">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli6" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani6">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani6" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es6">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es6" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli7">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli7" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani7">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani7" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es7">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es7" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli8">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli8" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani8">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani8" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es8">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es8" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli9">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli9" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani9">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani9" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es1">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es9" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli10">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli10" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani10">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani10" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es10">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es10" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli11">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli11" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani11">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani11" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es11">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es11" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli12">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli12" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani12">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani12" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es12">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es12" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli13">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli13" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani13">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani13" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es13">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es13" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli14">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli14" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani14">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani14" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es14">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es14" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli15">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli15" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani15">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani15" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es15">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es15" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli16">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli16" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani16">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani16" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es16">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es16" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli17">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli17" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani17">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani17" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es17">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es17" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli18">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli18" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani18">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani18" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es18">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es18" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli19">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli19" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani19">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani19" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es19">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es19" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli20">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli20" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani20">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani20" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es20">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es20" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli21">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli21" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani21">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani21" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es21">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es21" />
                                                <br/>
                                                <hr />
						<label style="font:caption" for="rooli22">Roolin nimi tai muu tehtävä:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "rooli22" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="aani22">Roolin ääniala tai tehtävän nimike:</label>
                                                <br/>
                                                <input type = "text" size = "40" maxlength ="40" name = "aani22" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="es22">Onko kyseessä esiintyjä?</label>
                                                <input type="checkbox" checked="checked" value="on" name="es22" />
                                                <br/>
                                                <hr />
						<input type="submit" name="save" value="save" />
					</form>
				</td>
			</tr>
		</table>
	</body>

</html>
