<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<form action="/koosta_esitys" method="GET">
		<h3 align="center">Lisää esitykseen esittäjiä, taustahenkilöitä ja ryhmiä</h3>
		<p align="center">Kaikki sivun tiedot lähetevät, kun mitä tahansa save-nappuloista painetaan.</p>
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="70%" bgcolor="#dddddd" align="center">
					<h6>Tietokannassa olevat koostamiskelpoiset esitykset<br />Yhdistä esiintyjät ja taustatehtävät henkilöihin</h6>
					<table border="4" width="100%">
							<input type="hidden" name="roolilkm" value="{{roolilkm}}" />
							<input type="hidden" name="esitys_id" value="{{esi_id}}" />
							%i = 1
							<tr>
									%if len(esitys) > 0:
										<td>{{esitys[0][2]}}:<br />
											{{esitys[0][3]}},<br />
											{{esitys[0][6]}}
										</td>
									%end
							</tr>
							%for item in esitys:
								%rooli_id = 'rooli_id' + str(i)
								%henkilo_id = 'henkilo_id' + str(i)
								<input type="hidden" name="{{rooli_id}}" value="{{item[1]}}" />
								<tr>
									<td>{{item[4]}}</td>
									<td>{{item[5]}}</td>
									<td>
										<label for="{{henkilo_id}}"><h6>Valitse tietokannasta henkilö</h6></label>	
										<select name="{{henkilo_id}}" accesskey="">
											<option value="-1" selected="selected">Valitse:</option>
											%for item in henkilot:
												<option value="{{item[0]}}">{{item[1]}}:	{{item[2]}}, {{item[3]}}</option>
											%end
										</select>
									</td>

								</tr>
								%i = i + 1
							%end
							<br />
							<td>
								<input type="submit" name="save" value="save" />	
							</td>
					</table>
				</td>
				<td align="center" width="30%" bgcolor="#cccccc">
					<h6>Lisää tällä lomakkeella ryhmiä esitykseen</h6>
					<input type="submit" name="save" value="save" />	
					<select name="ryhma1" accesskey="">
                                        	<option value="-1" selected="selected">Valitse:</option>    
                                                	%for item in ryhmat:    
                                                        	<option value="{{item[0]}}">{{item[1]}}, {{item[2]}}</option>
                                                        %end    
                                        </select>
 					<hr />
					<select name="ryhma2" accesskey="">
                                        	<option value="-1" selected="selected">Valitse:</option>    
                                                	%for item in ryhmat:    
                                                        	<option value="{{item[0]}}">{{item[1]}}, {{item[2]}}</option>
                                                        %end    
                                        </select>
 					<hr />
					<select name="ryhma3" accesskey="">
                                        	<option value="-1" selected="selected">Valitse:</option>    
                                                	%for item in ryhmat:    
                                                        	<option value="{{item[0]}}">{{item[1]}}, {{item[2]}}</option>
                                                        %end    
                                        </select>
 					<hr />
				</td>
			</tr>
		</table>
		</form>
	</body>
</html>
