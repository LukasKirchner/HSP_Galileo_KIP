<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="org.python.core.PyException" %>
<%@ page import="org.python.core.PyInteger" %>
<%@ page import="org.python.core.PyObject" %>
<%@ page import="org.python.util.PythonInterpreter" %>
<%@ page import="java.util.Properties" %>
<%@ page import="java.io.File" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>HSP Galileo KIP</title>
</head>
<body>
<h1>HSP Galileo KIP</h1>

  <%
  String[] settings_str = request.getParameterValues("settings");
  String[] csv_str = request.getParameterValues("csv");
  String[] outputFileName_str = request.getParameterValues("output");
  String[] numberOfOutputFiles_str = request.getParameterValues("numberOfOutputFiles");
  
  if (csv_str == null || csv_str[0].isEmpty()) {
	  csv_str = request.getParameterValues("csv_hidden");
  }
  if (settings_str == null || settings_str[0].isEmpty()) {
	  settings_str = request.getParameterValues("settings_hidden");
  }
  
  if(outputFileName_str == null) {
	  outputFileName_str = new String[1];
	  outputFileName_str[0] = ("HSP_Galileo_KIP");
  }
  if (outputFileName_str[0].isEmpty()) {
	  outputFileName_str[0] = "HSP_Galileo_KIP";
  }
  
  if(numberOfOutputFiles_str == null) {
	  numberOfOutputFiles_str = new String[1];
	  numberOfOutputFiles_str[0] = "10"; 
  }
  if(numberOfOutputFiles_str[0].isEmpty()) {
	  numberOfOutputFiles_str[0] = "10";  
  }
  
  %>

<form method="get" action="#">
	<p>
		Settings file:
		<input type="file" name="settings">
		<input type="hidden" name="settings_hidden" value="
			<% if (settings_str != null && settings_str[0] != null) { %>
				<%= settings_str[0] %>
			<% } %>
		">
	</p>
	<p>
		CSV file:
		<input type="file" name="csv">
		<input type="hidden" name="csv_hidden" value="
			<% if (csv_str != null && csv_str[0] != null) { %>
				<%= csv_str[0] %>
			<% } %>
		">
	</p>
	<p>
		Output file name:
		<input type="text" name="output" value="<% if(outputFileName_str == null || outputFileName_str[0] == null ) { %><% outputFileName_str[0] = "HSP_Galileo_KIP_out"; %><% }%><%= outputFileName_str[0] %>">
	</p>
	<p> 
		Number of images:
		<input type="text" name="numberOfOutputFiles" value="<% if(numberOfOutputFiles_str == null || numberOfOutputFiles_str[0] == null ) { %><% numberOfOutputFiles_str[0] = "10"; %><% }%><%= numberOfOutputFiles_str[0] %>">
	</p>
	<p>
		<input type="submit"></input>
	</p>
</form>

  <% if (settings_str != null && csv_str != null) {
  %>	
		<% 
		
		String pythonPath = "C:\\Python_2_7";
		String pythonProgram = "HSP_Galileo_KIP";
		
		Runtime rt = Runtime.getRuntime();
		Process pr = rt.exec("C:\\bat\\pythonpath.bat" + " " 
			+ pythonPath + " " 
			+ pythonProgram + " " 
			+ settings_str[0] + " "
			+ csv_str[0] + " "
			+ outputFileName_str[0] + " "
			+ numberOfOutputFiles_str[0]);
		   	
		%>
		
		<% 
		Integer numberOfOutputFiles = 10;
		try {
			numberOfOutputFiles = Integer.parseInt(numberOfOutputFiles_str[0]);
		} catch (NumberFormatException e){
			System.out.println(e);
		} finally {
			if(numberOfOutputFiles == null || numberOfOutputFiles < 1){
				numberOfOutputFiles = 10;
			}
		}

		String pathToImages = "img";
		int i = 0;
		for(;i<numberOfOutputFiles;i++){ 
			%>
			<p>
				<img src="<%= pathToImages + File.separator + outputFileName_str[0] + "_" + i + ".png" %> ">
			</p>
			<%
		}
		%>				
  <%
  }
  %>
</body>
</html>