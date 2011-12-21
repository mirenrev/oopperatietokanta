<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3 align="center">Valitse koostettava esitys</h3>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="60%" bgcolor="#dddddd" align="center">
					<h6>Tietokannassa jo olevat esitykset</h6>
					<table border="4" width="100%">
					%for item in esitykset:
						<tr>
							<td>{{item[1]}}</td>
							<td>{{item[2]}}</td>
							<td>{{item[3]}}</td>
						</tr>
					%end
					</table>
				</td>
				<td width="40%" bgcolor="#cccccc" align="center">
					<h6>Valitse esitys tästä</h6>
					<form action="/koosta_esitys" method="GET">
						<label for="esitys_id"><h6>Valitse olemassa oleva esitys tästä.<br />Siirry yhdistelemään tietoja.</h6></label>   
                                                <select name="esitys_id" accesskey="">
                                                	<option value="-1" selected="selected">Valitse:</option>    
                                                        %for item in esitykset:    
                                                                <option value="{{item[0]}}">{{item[1]}}:     {{item[2]}}, {{item[3]}}</option>
                                                        %end    
                                                </select>
                                                <input type="submit" name="Koostamaan" value="Koostamaan" />
                                                <hr />

					</form>
				</td>
			</tr>
		</table>

	</body>

</html>
