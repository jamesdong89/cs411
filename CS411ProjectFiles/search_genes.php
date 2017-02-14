<?php

	$link = mysql_connect('webhost.engr.illinois.edu', 'projectdemo411_cs411', 'cs411');
	if (!$link) {
		die('Could not connect: ' . mysql_error());
	}
	mysql_select_db('projectdemo411_cs411');


	$searchCriterion=$_POST["search_param"];
	$searchType=$_POST["search_type"];


	if ($searchType == "Gene No.")
	{
		$sql="SELECT * FROM Gene WHERE Gene_No = '$searchCriterion' ORDER BY Gene_ID";

	}

	else if ($searchType == "Gene ID")
	{
		$sql="SELECT * FROM Gene WHERE Gene_ID = '$searchCriterion' ORDER BY Gene_Full_Name";
	}
	else if ($searchType == "Gene Symbol")
	{
		$sql="SELECT * FROM Gene WHERE Gene_Symbol LIKE '%$searchCriterion%' ORDER BY Gene_Full_Name";
	}
	else
	{
		$sql="SELECT * FROM Gene WHERE Gene_Full_Name LIKE '%$searchCriterion%' ORDER BY Gene_Full_Name";
	}


	$res=mysql_query($sql);
	
		
	print("<table width=\"100%\" border=\"1\" cellpadding=\"10\"> 
		<tr>
			<td  align=\"center\">
			<h1>Gene Information Database</h1>
			<h2> CS411 </h2>
			<h3>For Demo Purpose Only!</h3>
			<h4>Gene Search Result(s)</h4>
			</td>
		</tr> ");
		
	print("<td>&nbsp;<a href=\"index.html\">Home</a> &nbsp;
	     </td> ");
	
	print("<tr>
			<td align=\"center\"> ");
			

			if (mysql_num_rows($res)>0)
			{
				print("<p>There are " . mysql_num_rows($res) . " result(s) available</p>");
				while($data=mysql_fetch_assoc($res))
				{
					print("<p><b> Gene: {$data['Gene_No']} </b>");
			  
					print("<br><br>");

					print("<b><u>Gene ID:</u></b> {$data['Gene_ID']}<br/>");
					print("<b><u>Gene Symbol:</u></b> {$data['Gene_Symbol']}<br/>");
					print("<b><u>Gene Name:</u></b> {$data['Gene_Full_Name']}<br/>");
					print("<b><u>Gene Function:</u></b> {$data['Gene_Function']}<br/>");
					print("<b><u>Gene Length:</u></b> {$data['Gene_Length']}<br/>");
					print("<br><br>"); 
				}
			}
			else
			{
				print("There is no gene found with your current search criterion  :-  $searchType = \"$searchCriterion\" <br> Please recheck your searching criteria! <br\> <br> Thanks! <br/>");
			}
			
		
			print("</td>
		</tr>
		
	</table> ");		
	mysql_close($link);



?>


