<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.io.File" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>HSP Galileo KPI</title>
</head>
<body>
<h1>HSP Galileo KIP</h1>
<% 
	File folder = new File("C:\\csv\\");
	File[] files = folder.listFiles();
%>

<%
	String[] csv_str = request.getParameterValues("csv"); 
	String csv;
	if(csv_str != null){
		csv = csv_str[0];
	} else if (files != null && files.length > 0) {
		csv = files[0].getAbsolutePath();
	} else {
		csv = "";
	}
	
	String[] numberOfOutputFiles_str = request.getParameterValues("numberOfOutputFiles");
	String numberOfOutputFiles;
	if(numberOfOutputFiles_str != null){
		numberOfOutputFiles = numberOfOutputFiles_str[0];
	} else {
		numberOfOutputFiles = "0";
	}
	
%>

<form method="get" action="#" >
	<p>
		<label> CSV input file:
			<select name="csv" >
				<% for (File file : files) { %>		
					<% String selected = csv.equals(file.getAbsolutePath()) ? "selected" : ""; %>
					<option <%= selected %>><%= file.getAbsolutePath() %></option>
				<% } %>
			</select>	
		</label>
	</p>
	<p> 
		Number of images:
		<input type="text" name="numberOfOutputFiles" value="<%= numberOfOutputFiles %>">
	</p>
	<p>
		You can change the settings <a href="http://localhost:8080/HSP_Galileo_KIP/Settings.jsp">here</a>.
	</p>
	<p>
		<input type="submit"></input>
	</p>
</form>

<% 	
	String pythonPath = "C:\\Python_2_7";
	String pythonProgram = "HSP_Galileo_KIP";
	String settings = "C:\\conf\\conf.conf";
	String outputFileName = "out";
	
	if(csv != null && csv.isEmpty() == false){
		
		Runtime rt = Runtime.getRuntime();
		Process pr = rt.exec("C:\\bat\\pythonpath.bat" + " " 
			+ pythonPath + " " 
			+ pythonProgram + " " 
			+ settings + " "
			+ csv + " "
			+ outputFileName + " "
			+ numberOfOutputFiles);
	}
%>
<%	
	Integer numberOfImages = 10;
	try {
		numberOfImages = Integer.parseInt(numberOfOutputFiles_str[0]);
	} catch (NumberFormatException e){
		System.out.println(e);
	} catch (NullPointerException e2){
		numberOfImages = 0;
	}
	
	String pathToImages = "img";
	int i = 0;
	for(;i<numberOfImages;i++){ 
		%>
		<p>
			<img src="<%= pathToImages + File.separator + outputFileName + "_" + i + ".png" %> ">
		</p>
		<%
	}
	%>

</body>
</html>