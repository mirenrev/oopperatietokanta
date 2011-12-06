<html>
	<head>
	</head>

	<body>
		<h3 align="center">Lisää tietokantaan ooppera</h3>
		<div align="center">
			<h6>Tietokannassa jo olevat oopperat</h6>
			<table border = "4", width = "100">
			%for item in rivit:
				<tr>
					<td>{{item[0]}}</td>
					<td>{{item[1]}}</td>
				</tr>
			%end
			</table>
			<hr />
			<form action="/lisaa" method="GET">
				<input type = "text" size="50" maxlength="40" name="oopnimi" value = "Oopperan nimi"/>
				<br/>
				<input type = "text" size = "50" maxlength ="40" name = "saveltaja" value = "Oopperan säveltäjä"/>
				<br/>
				<input type="submit" name = "save" value = "save"/>
			</form>
		</div>
	</body>
</html>
