import requests as req
import json

url = ''
response = req.get(url)
data = response.json()

for row in data:
    print(row)
