import requests

cookies = {"magshim_manager": "python_is_better_than_c"}
URL = "http://secret.magshimail.com/secret.php"

response = requests.post(URL, cookies=cookies)
print(response.text)
