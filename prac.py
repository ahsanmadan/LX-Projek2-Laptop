import requests

url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/nay?key=a222de28-5651-402e-8a5d-222fcd2263ef'
r = requests.get(url)
result = r.json()
print(result)