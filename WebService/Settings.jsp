<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.io.File" %>
<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.FileReader" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.List" %>
<%@ page import="main.Setting" %>
<%@ page import="java.net.*" %>
<%@ page import="java.io.*" %>
<%@ page import="java.util.*" %>
<%@ page import="main.FileWriterHelper"%>
<%@ page import="main.FileReaderHelper"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Change HSP Galileo KIP settings here</title>
</head>
<body>
<h1>HSP Galileo KIP settings</h1>

<% 	URL url = new URL("http://localhost:8080/HSP_Galileo_KIP/settings/conf.conf"); // for download
	
	File file = new File("C:\\conf\\conf.conf"); // for upload
	List<Setting> settings = new ArrayList<Setting>(); 
%>

<% // write settings file

	Enumeration<String> names_enum = request.getParameterNames();
		
	int namesNumber = 0;
	while(names_enum.hasMoreElements() == true){
		names_enum.nextElement();
		namesNumber++;
	}
	String[] names = new String[namesNumber];
	String[] values = new String[namesNumber];
	names_enum = request.getParameterNames();
	int j=0;
	for(;j<namesNumber;j++){
		names[j] = names_enum.nextElement();
		values[j] = request.getParameterValues(names[j])[0];
	}
	
	List<Setting> settingsForWriting = new ArrayList<Setting>(); 
	if(names != null && names.length > 0 && values != null && values.length > 0 && names.length == values.length) {		
		int counter = 0;
		for(;counter< names.length; counter++){
			settingsForWriting.add(new Setting(names[counter], values[counter]));
		}
		FileWriterHelper.writeListToFile(settingsForWriting, file);
	}
	
%>

<% // read settings file
	settings = FileReaderHelper.readFile(file);
%>

<form method="get" action="#">
	<% for (Setting setting : settings) { %>
	<p>
		<%= setting.getNameOfSetting() %>: <input type="text" name="<%= setting.getNameOfSetting() %>" value="<%= setting.getValueOfSetting() %>" >
	</p>
	<% } %>
	<p>
		<input type="submit"></input>
	</p>
</form>

<h2>Settings</h2>
Back to the HSP Galileo KPI tool by clicking <a href="http://localhost:8080/HSP_Galileo_KIP/Main.jsp">here</a>.

</body>
</html>