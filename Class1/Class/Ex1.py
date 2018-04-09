import requests

URL = "http://hmpg.net"
response = requests.get(URL)
html = response.text
print(html)