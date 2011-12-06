<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
		<h3 align="center">Lisää tietokantaan ooppera</h3>
<!--		<div align="center">-->
		<table width="100%" height="100%" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td width="70%" bgcolor="#dddddd" align="center">
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
				<td width="30%" bgcolor="#cccccc" height="100%" align="center">
					<h6>Kirjoita tähän lisättävän oopperan tiedot</h6>
					<form action="/lisaa" method="GET">
						<input type = "text" size="50" maxlength="40" name="oopnimi" value = "Oopperan nimi"/>
						<br/>
						<input type = "text" size = "50" maxlength ="40" name = "saveltaja" value = "Oopperan säveltäjä"/>
						<br/>
						<input type="submit" name = "save" value = "save"/>
					</form>
				</td>
			</tr>	
		</table>
<!--		</div>-->
	</body>
</html>
