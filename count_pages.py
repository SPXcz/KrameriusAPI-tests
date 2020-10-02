import json
import requests

query = "http://kramerius.mzk.cz/search/api/v5.0/item/{}/children".format('uuid:530719f5-ee95-4449-8ce7-12b0f4cadb22')

response = requests.get(query)

filterResult = len(list(filter(lambda prvek: prvek['details']['type'] == 'NormalPage', response.json())))

print(filterResult)