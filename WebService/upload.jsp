<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.net.*" %>
<%@ page import="java.io.*" %>
<%@ page import="java.io.*,java.util.*, javax.servlet.*" %>
<%@ page import="javax.servlet.http.*" %>
<%@ page import="org.apache.commons.fileupload.*" %>
<%@ page import="org.apache.commons.fileupload.disk.*" %>
<%@ page import="org.apache.commons.fileupload.servlet.*" %>
<%@ page import="org.apache.commons.io.output.*" %>
<%@ page import="java.net.*" %>
<%@ page import="java.io.*" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>HSP Galileo KIP upload csv</title>
</head>
<body>
<h1>HSP Galileo KIP upload csv</h1>

Select a file to upload: <br />
<form action="uploadCsv.jsp" method="post" enctype="multipart/form-data">
    <p>
    	<input type="file" name="file" size="50" />
    </p>
    <p>
    	<input type="submit" value="Upload File" />
    </p>
</form>

<% URL webAddress = new URL("http://localhost:8080/HSP_Galileo_KIP/"); %>
Back to the HSP Galileo KPI tool by clicking <a href="<%= webAddress.getPath() %>index.jsp">here</a>.

</body>
</html>