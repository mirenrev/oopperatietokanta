<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3>Lisää tietokantaan esiintyjien ja taustahenkilöiden tietoja</h3>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="60%" bgcolor="#dddddd" align="center">
					<h6>Tietokannassa jo olevat esiintyjät ja taustahenkilöt</h6>
					<table border="4" width="100%">
						%for item in rivit:
							<tr>
								<td>{{item[1]}}, {{item[2]}}: {{item[3]}}</td>
							</tr>				
						%end
					</table>	
				</td>
				<td width="40%" bgcolor="#cccccc" align="center">
					<h6>Lisää uusia esiintyjiä ja taustahenkilöitä tällä lomakkeella.</h6>
					<form action="/lisaa_henkiloita" method="GET">
						<input type="submit" name="save" value="save">
						<br />
                                                <hr />
						<label style="font:caption" for = "etunimi1">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi1" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi1">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi1" value = ""/>
						<br />
						<label style="font:caption" for="ammatti1">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti1" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi2">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi2" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi2">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi2" value = ""/>
						<br />
						<label style="font:caption" for="ammatti2">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti2" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi3">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi3" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi3">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi3" value = ""/>
						<br />
						<label style="font:caption" for="ammatti3">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti3" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi4">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi4" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi4">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi4" value = ""/>
						<br />
						<label style="font:caption" for="ammatti4">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti4" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi5">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi5" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi5">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi5" value = ""/>
						<br />
						<label style="font:caption" for="ammatti5">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti5" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi6">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi6" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi6">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi6" value = ""/>
						<br />
						<label style="font:caption" for="ammatti6">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti6" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi7">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi7" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi7">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi7" value = ""/>
						<br />
						<label style="font:caption" for="ammatti7">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti7" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi8">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi8" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi8">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi8" value = ""/>
						<br />
						<label style="font:caption" for="ammatti8">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti8" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi9">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi9" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi9">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi9" value = ""/>
						<br />
						<label style="font:caption" for="ammatti9">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti9" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi10">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi10" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi10">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi10" value = ""/>
						<br />
						<label style="font:caption" for="ammatti10">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti10" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi11">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi11" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi11">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi11" value = ""/>
						<br />
						<label style="font:caption" for="ammatti11">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti11" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi12">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi12" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi12">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi12" value = ""/>
						<br />
						<label style="font:caption" for="ammatti12">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti12" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi13">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi13" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi13">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi13" value = ""/>
						<br />
						<label style="font:caption" for="ammatti13">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti13" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi14">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi14" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi14">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi14" value = ""/>
						<br />
						<label style="font:caption" for="ammatti14">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti14" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi15">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi15" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi15">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi15" value = ""/>
						<br />
						<label style="font:caption" for="ammatti15">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti15" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi16">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi16" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi16">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi16" value = ""/>
						<br />
						<label style="font:caption" for="ammatti16">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti16" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi17">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi17" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi17">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi17" value = ""/>
						<br />
						<label style="font:caption" for="ammatti17">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti17" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi18">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi18" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi18">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi18" value = ""/>
						<br />
						<label style="font:caption" for="ammatti18">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti18" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi19">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi19" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi19">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi19" value = ""/>
						<br />
						<label style="font:caption" for="ammatti19">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti19" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi20">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi20" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi20">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi20" value = ""/>
						<br />
						<label style="font:caption" for="ammatti20">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti20" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi21">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi21" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi21">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi21" value = ""/>
						<br />
						<label style="font:caption" for="ammatti21">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti21" value=""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "etunimi22">Etunimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="etunimi22" value = ""/>
                                                <br/>
                                                <label style="font:caption" for="sukunimi22">Sukunimi</label>
                                                <br />
                                                <input type = "text" size = "40" maxlength ="40" name = "sukunimi22" value = ""/>
						<br />
						<label style="font:caption" for="ammatti22">Tehvävä (esim. sopraano tai lavastaja)</label>
						<br />
						<input type="text" size="40" maxlength="40" name="ammatti22" value=""/>
                                                <br/>
						<hr />
						<input type="submit" name="save" value="save">
						<br />
                                                <hr />

					</form>
				</td>
			</tr>
		</table>
		
	</body>
</html>
