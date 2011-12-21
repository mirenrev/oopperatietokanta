<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3 align="center">Lisää esityspäivä ja liitä se oopperataloon ja esitettyyn oopperaan</h3>
                <table width="100%" height="100%" cellspacing="0" cellpadding="10">
                        <tr valign="top">
                                <td width="60%" bgcolor="#dddddd" align="center">
                                        <h6>Tietokannassa jo olevat oopperatalot</h6>
					<table border="4" width="100%">
					%for item in ooptalot:
						<tr>    
 							<td>{{item[1]}}</td>
 							<td>{{item[2]}}</td>
						</tr>

					%end
					</table>
					<h6>Tietokannassa jo olevat oopperat</h6>
                                        <table border="4" width="100%">
                                        %for item in ooplista:
                                                <tr>
                                                        <td>{{item[1]}}</td>
                                                        <td>{{item[2]}}</td>
                                                </tr>
                                        %end
                                        </table>
				</td>
				<td width="40%" bgcolor="#cccccc" align="center">
					<form action="/lisaa_espaiva" method="GET">
						<h6>Syötä päivämäärä tähän</h6>
						<label style="font:caption" for="paivamaara">Päivämäärä</label>
						<input type="text" size="40" maxlength="40" name="paivamaara" value="" />
						<br />
						<hr />
						<label for="ooppera_id"><h6>Valitse olemassa oleva ooppera tästä.</h6></label>   
                                                <select name="ooppera_id" id="ooppera_id" accesskey="">
                                                        <option value="-1" selected="selected">Valitse:</option>    
                                                        %for item in ooplista:    
                                                                <option value="{{item[0]}}">{{item[1]}}:     {{item[2]}}</option>
                                                        %end    
                                                </select>
						<label for="talo_id"><h6>Valitse oopperatalo tästä.</h6></label>
						<select name="talo_id" accesskey="">
							<option value="-1" selected="selected">Valitse:</option>
							%for item in ooptalot:
								<option value="{{item[0]}}">{{item[1]}}, {{item[2]}}</option>
							%end
						</select>
						<hr />
						<input type="submit" name="save" value="save" />
					</form>
	
				</td>
			</tr>
		</table>
	</body>
</html>
