<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.io.*" %>
<%@ page import="java.net.*" %>
<%@ page import="org.apache.commons.lang.SystemUtils.*" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>HSP Galileo KPI</title>
</head>
<body>
<h1>HSP Galileo KIP</h1>
<% 

	ServletContext sc = request.getSession().getServletContext();
	String path = sc.getRealPath("/");
	File localFolder = new File(path);
	
	URL webAddress = new URL("http://localhost:8080/HSP_Galileo_KIP/");

	String csvFolder = "csv";
	String imageFolder = "img";
	
	String scriptFolder = "script";
	String scriptFile = "pythonpath";
	
	String confFolder = "conf";
	String confFile = "conf.conf";
	
	String pythonFolder = "python";
	String pythonScript = "HSP_Galileo_KIP";
	String pythonVersion = "Python_2_7";
%>

<%
	String pythonPath = localFolder.getAbsolutePath() + File.separator + pythonVersion;
	String pythonProgram = localFolder.getAbsolutePath() + File.separator + pythonFolder + File.separator + pythonScript + ".py";	
%>

<%
	File localfolder = new File(localFolder.getAbsolutePath() + File.separator + csvFolder + File.separator);
	File[] files = localfolder.listFiles();

	File folderImages = new File(localFolder.getAbsolutePath() + File.separator + imageFolder + File.separator);
	File[] images = folderImages.listFiles();
%>

<%
	String[] csv_str = request.getParameterValues("csv"); 
	String csv;
	if(csv_str != null){
		csv = csv_str[0];
	} else if (files != null && files.length > 0) {
		csv = files[0].getName();
	} else {
		csv = "";
	}	
%>

<form method="get" action="#" >
	<p>
		<label> CSV input file:
			<select name="csv" >
				<% for (File file : files) { %>		
					<% String selected = csv.equals(file.getName()) ? "selected" : ""; %>
					<option <%= selected %>><%= file.getName() %></option>
				<% } %>
			</select>	
		</label>
	</p>
	<p>
		You can change the settings <a href="<%= webAddress.getPath() %>settings.jsp">here</a>.
	</p>
	<p>
		You can upload new csv files <a href="<%= webAddress.getPath() %>upload.jsp">here</a>.
	</p>
	<p>
		<input type="submit"></input>
	</p>
</form>

<% 	

	String windowsScript = localFolder.getAbsolutePath() + File.separator + scriptFolder + File.separator + scriptFile + ".bat";
	String linuxMacScript = "sh" + localFolder.getAbsolutePath() + File.separator + scriptFolder + File.separator + scriptFile + ".sh";
			
	String script;
	//if(org.apache.commons.lang.SystemUtils.IS_OS_WINDOWS){
		script = windowsScript;
	/*} else {
		script = linuxMacScript;
	}*/		

	String command = script + " " 
		+ pythonPath + " " 
		+ pythonProgram + " " 
		+ localFolder.getAbsolutePath() + File.separator + confFolder + File.separator + confFile + " "
		+ localFolder.getAbsolutePath() + File.separator + csvFolder + File.separator + csv + " "
		+ folderImages.getAbsolutePath();

	if(csv != null && csv.isEmpty() == false){
		Runtime rt = Runtime.getRuntime();
		Process pr = rt.exec(command);
	}
%>

<%	if(images != null){
		for(File image : images){ 
			%>
			<p>
				<img src="<%= webAddress.getPath() + "/" + imageFolder + "/" + image.getName() %> ">
			</p>
			<%
		}
	}
%>

</body>
</html>