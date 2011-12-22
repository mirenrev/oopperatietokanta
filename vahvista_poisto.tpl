<html>
	<head>
	</head>

	<body bgcolor="#eeeeee">
                <p>Navigointi: <a href="/pikahaku">Pikahakuun</a> <a href="/tarkhaku">Tarkennettuun hakuun</a> <a href="/lisaa_ooppera">Siirry lisäämään ooppera</a> <a href="/lisaa_henkiloita">Siirry lisäämään henkilöitä</a> <a href="/lisaa_oopperataloja">Siirry lisäämään oopperataloja</a> <a href="/lisaa_espaiva">Lisää esityspäivä</a> <a href="/lisaa_ryhmia">Lisää ryhmiä</a> <a href="/koosta_esitys">Koosta annetuista tiedoista esitys</a></p>
		<h3 align="center">Tiedon poiston vahvistus</h3>
		<p>Haluatko poistaa tietokannasta kokonaan tiedon {{arvo}} taulusta {{taulu}}?</p>
		<hr />
		<br />
		<form action="/muokkaa_henkiloa">
			<input type="submit" name="Vahvista" value="Vahvista" />
			<input type="submit" name="Peru" value="Peru">
			<input type="hidden" name="id" value="{{_id}}"/>
			<input type="hidden" name="id_arvo" value="{{_id_arvo}}"/>
			<input type="hidden" name="taulu" value="{{taulu}}"/>
		</form>
	</body>
</html>
