<html>
	<head>
	</head>

	<body bgcolor='#eeeeee'>
		<h3 align="center">Lisää tietokantaan ryhmia</h3>
                <table width="100%" height="100%" cellspacing="0" cellpadding="10">
                        <tr valign="top">
                                <td width="60%" bgcolor="#dddddd" align="center">
                                        <h6>Tietokannassa jo olevat ryhmat</h6>
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
					<h6>Lisää ryhmia ja niiden tehtavia tällä lomakkeella</h6>
					<form action="/lisaa_ryhmia" method="GET">
						<input type="submit" name="save" value="save" />
						<br />
						<hr />
						<label style="font:caption" for = "ryhmannimi1">Ryhmän nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmannimi1" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ryhmantehtava1">Ryhmän tehtävä:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmantehtava1" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ryhmannimi2">Ryhmän nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmannimi2" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ryhmantehtava2">Ryhmän tehtävä:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmantehtava2" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ryhmannimi3">Ryhmän nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmannimi3" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ryhmantehtava3">Ryhmän tehtävä:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmantehtava3" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ryhmannimi4">Ryhmän nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmannimi4" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ryhmantehtava4">Ryhmän tehtävä:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmantehtava4" value = ""/>
                                                <br/>
						<hr />
						<label style="font:caption" for = "ryhmannimi5">Ryhmän nimi:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmannimi5" value = ""/>
                                                <br/>
						<label style="font:caption" for = "ryhmantehtava5">Ryhmän tehtävä:</label>
                                                <br />
                                                <input type = "text" size="40" maxlength="40" name="ryhmantehtava5" value = ""/>
                                                <br/>
						<hr />
						<input type="submit" name="save" value="save" />
					</form>
				</td>
			</tr>
		</table>
	</body>
</html>
