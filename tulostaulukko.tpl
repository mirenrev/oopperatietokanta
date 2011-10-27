<html>
<head>
	<title>Tulossivu</title>
</head>




<body>
%# Malli tulostaulukon luontiin
<p>Hakutulokset</p>


%for i in range(len(rivit[0])):
<table border="10" width = "400">
	<th>Ooppera</th>
	%for item in rivit[0][i]:
		<tr>
			<td align ="center">{{item}} </td>
		</tr>
	%end	 

	<th>Toteuttajat</th>
	%for jtem in rivit[1][i]:
		<tr>
		%for x in jtem:
				<td align="center">{{x}}</td>
		%end
		</tr>
	%end
	<th>Ryhmät</th>
	%for ktem in rivit[2][i]:
		<tr>
		%for y in ktem:
			<td align="center">{{y}}</td>
		%end
		</tr>
	%end
</table>
%end

</body>
</html>
