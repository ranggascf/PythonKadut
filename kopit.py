import json
import requests

dataindonesia = 'https://api.kawalcorona.com/indonesia'

def data_covid():
    Response = requests.get(dataindonesia)
    data = json.loads(Response.text)
    return str(data)

print(data_covid())