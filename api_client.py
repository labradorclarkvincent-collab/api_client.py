import requests

url = &quot;https://YOUR-URL.onrender.com/student&quot;
response = requests.get(url)
if response.status_code == 200:
data = response.json()
print(&quot;Student ID:&quot;, data[&quot;student_id&quot;])
print(&quot;Name:&quot;, data[&quot;name&quot;])
print(&quot;Program:&quot;, data[&quot;program&quot;])
print(&quot;Year:&quot;, data[&quot;year&quot;])
print(&quot;Section:&quot;, data[&quot;section&quot;])
else:
print(&quot;Request failed.&quot;)
print(&quot;Status Code:&quot;, response.status_code)
