import requests

req = requests.get("https://geo.api.qualaroo.com/")
req1 = requests.get('http://httpbin.org/get', params=payload)
info = req.json()
print(info)
print(info['city'])
print(info['country_code2'])
