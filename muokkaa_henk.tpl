<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
        	<h3 align="center">Lisää tietokantaan ooppera ja rooleja</h3>
        	<table width="100%" height="100%" cellspacing="0" cellpadding="10">
                	<tr valign="top">
                        	<td width="60%" bgcolor="#dddddd" align="center">
                                	<h6>Tietokannassa olevat henkilöt</h6>
                                        <table border="4" width="100%">
                                        %for item in rivit:
                                                <tr>
                                                        <td>{{item[2]}}</td>
                                                        <td>{{item[1]}}</td>
							<td>{{item[3]}}</td>
                                                </tr>
                                        %end
                                        </table>
                                </td>
                                <td width="40%" bgcolor="#cccccc" height="100%" align="center">
                                        <form action="/lisaa_ooppera" method="GET">
                                                <label for="henkilo"><h6>Valitse muokattavan henkilön tiedot tästä.</h6></label>   
                                                <select name="henkilo" id="" accesskey="">
                                                        <option value="-1" selected="selected">Valitse:</option>    
                                                        %for item in rivit:    
                                                                <option value="{{item[0]}}">{{item[2]}}, {{item[1]}}:     {{item[3]}}</option>
                                                        %end    
                                                </select>
						<br />
						<hr />
						<label style="font:caption" for="etunimi">Uusi etunimi:</label>
						<br />
						<input type="text" size="20" maxlength"40" name="etunimi" value="">
						<br />
						<br />
						<label style="font:caption" for="sukunimi">Uusi sukunimi:</label>
						<br />
						<input type="text" size="20" maxlength"40" name="sukunimi" value="">
						<br />
						<br />
						<label style="font:caption" for="ammatti">Uusi ammatti, ääniala tms.</label>
						<br />
						<input type="text" size="20" maxlength"40" name="ammatti" value="">
						<br />
						<br />
                                                <input type="submit" name="save" value="save" />
                                                <hr />
                                        </form>
			</tr>
		</table>

		
	</body>
</html>
