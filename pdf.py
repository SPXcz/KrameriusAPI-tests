import json
import requests
import xml.etree.ElementTree as ET

uuidArray = ['uuid:aa6235b0-b28e-11e3-bb86-005056825209', 'uuid:3fea3b46-82af-4922-b784-54c44b97edba']

query = "http://krameriusadmin.mzk.cz/search/api/v5.0/pdf/selection?pids="

for uuid in uuidArray:
    query = query + uuid + ","

query = query.replace(uuid[-1]+",", uuid[-1])

print(query)

response = requests.get(query)

print(response)