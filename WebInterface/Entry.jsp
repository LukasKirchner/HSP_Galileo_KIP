<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="org.python.core.PyException" %>
<%@ page import="org.python.core.PyInteger" %>
<%@ page import="org.python.core.PyObject" %>
<%@ page import="org.python.util.PythonInterpreter" %>
<%@ page import="java.util.Properties" %>
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
  
  if (csv_str == null || csv_str[0].isEmpty()) {
	  csv_str = request.getParameterValues("csv_hidden");
  }
  if (settings_str == null || settings_str[0].isEmpty()) {
	  settings_str = request.getParameterValues("settings_hidden");
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
		<input type="submit"></input>
	</p>
</form>

  <% if (settings_str != null && csv_str != null) {
  %>
		<%= settings_str[0] %>
		<%= csv_str[0] %>
		
		<% String[] images = {"picture 1","picture 2","picture 3"};  %>
		
		<% for (String image : images) { %>
		<p>
			<%= image %>
		</p>
		<% } %>
		
		<!-- <%= java.lang.System.getProperty("user.home") %>  -->
		
		<% 
		
		Properties props = new Properties();
		props.put("python.home","C:\\jython2.7.0\\Lib");
		props.put("python.console.encoding", "UTF-8"); // Used to prevent: console: Failed to install '': java.nio.charset.UnsupportedCharsetException: cp0.
		props.put("python.security.respectJavaAccessibility", "false"); //don't respect java accessibility, so that we can access protected members on subclasses
		props.put("python.import.site","false");
		Properties preprops = System.getProperties();
		PythonInterpreter.initialize(preprops, props, new String[0]);
		
		PythonInterpreter interp = new PythonInterpreter(); 
		
		interp.exec("import sys");
			//interp.exec("python.home");
		interp.exec("sys.path.append('./WEB-INF/lib/py/')");
		interp.exec("sys.path.append(r'C:/jython2.7.0/Lib/')");
		interp.exec("sys.path.append(r'C:/jython2.7.0/Lib/site-packages/')");
		interp.exec("sys.path.append(r'C:/jython2.7.0/Lib/site-packages/numpy/lib')");
		   	//interp.exec("import py.matplotlib.pyplot as plt");
		   	interp.exec("from matplotlib import pyplot as plt");
		   	
		   	interp.exec("from basemap import Basemap");
		   	//interp.exec("from lib.matplotlib import pyplot as plt");
		   	//interp.exec("from mpl_toolkits.basemap import Basemap");
		   	interp.exec("fig = plt.figure(figsize=(12,10))");
		   	interp.exec("ax1 = fig.add_subplot(111)");
		   	interp.exec("map = Basemap(ax=ax1, llcrnrlon=leftlon, llcrnrlat=leftlat,urcrnrlon=rightlon, urcrnrlat=rightlat,resolution='i', lat_0 = 0, lon_0 = 0)");
		   	interp.exec("img = plt.savefig('firstImage.png')");

		   					
		   	interp.set("a", new PyInteger(42));
		   	PyObject a = interp.get("a");
		   	interp.set("img", new PyInteger(43));
		   	PyObject img = interp.get("img");
		   	
		   	
		%>
		 <%= a %>
		<%= img %>
		
  <%
  }
  %>
</body>
</html>