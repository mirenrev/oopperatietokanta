%# Malli tulostaulukon luontiin
<p>Hakutulokset</p>

%for i in range(len(rivit[0])):
	%for item in rivit[0],rivit[1],rivit[2]:
		<table border="1">
		<tr>
			<td>	{{item[i]}} </td>
		</tr>
		<table>
	%end	 
%end





<table> 
%for rivi in rivit:
	<table border = "1">
		%for osuma in rivi:
			<tr>
				%for tulos in osuma:
					<td>{{tulos}}</td>
					<br/>
				%end
			</tr>
		%end
	</table>
%end
</table>

