%#Malli taulukon luontia varten
<p>Hakutulokset:</p>
<table border="1">
%for rivi in rivit:
	<tr>
	%for sarake in rivi:
		<td>{{sarake}}</td>
	%end
	</tr>
%end
</table>
