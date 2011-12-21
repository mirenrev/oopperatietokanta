<html>
	<head>
	</head>

	<body bgcolor='#eeeeee'>
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3 align="center">Lisää tietokantaan oopperataloja</h3>
                <table width="100%" height="100%" cellspacing="0" cellpadding="10">
                        <tr valign="top">
                                <td width="60%" bgcolor="#dddddd" align="center">
                                        <h6>Tietokannassa jo olevat oopperatalot</h6>
                                        <table border="4" width="100%">
                                        %for item in rivit:
                                                <tr>
                                                        <td>{{item[1]}}</td>
                                                        <td>{{item[2]}}</td>
                                                </tr>
                                        %end
                                        </table>
                                </td>
                                <td width="40%" bgcolor="#cccccc" height="100%" align="center">
					<h6>Lisää oopperataloja ja niiden sijainnit tällä lomakkeella</h6>
					<form action="/lisaa_oopperataloja" method="GET">
						<input type="submit" name="save" value="save" />
						<br />
						<hr />
						<label style="font:caption" for = "ooptalonnimi1">Oopperatalon nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonnimi1" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ooptalonsijainti1">Oopperatalon sijainti:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonsijainti1" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ooptalonnimi2">Oopperatalon nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonnimi2" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ooptalonsijainti2">Oopperatalon sijainti:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonsijainti2" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ooptalonnimi3">Oopperatalon nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonnimi3" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ooptalonsijainti3">Oopperatalon sijainti:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonsijainti3" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ooptalonnimi4">Oopperatalon nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonnimi4" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ooptalonsijainti4">Oopperatalon sijainti:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonsijainti4" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ooptalonnimi5">Oopperatalon nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonnimi5" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ooptalonsijainti5">Oopperatalon sijainti:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ooptalonsijainti5" value = ""/>
                                                <br/>
						<hr />
						<input type="submit" name="save" value="save" />
					</form>
				</td>
			</tr>
		</table>
	</body>
</html>
