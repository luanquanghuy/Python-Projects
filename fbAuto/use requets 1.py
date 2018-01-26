import requests


req = requests.get('https://cachhoc.net/')
print(req.encoding)
print(req.cookies)
print(req.url)
print(req.history)
print(req.status_code)
print(req.elapsed)
print(req.reason)
print(req.raw)
print(req.is_redirect)
# print(req.text)
print(req.headers)