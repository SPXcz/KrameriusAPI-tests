import json
import requests
import xml.etree.ElementTree as ET


query = "http://krameriusadmin.mzk.cz/search/api/v5.0/feed/mostdesirable"
response = requests.get(query)
print("Most desirable: https://krameriusadmin.mzk.cz/search/i.jsp?pid="+list(response.json()['data'])[0]['root_pid'])


query = "http://krameriusadmin.mzk.cz/search/api/v5.0/search?q={}".format('wh')


response = requests.get(query)

if response.status_code < 400:
    xml = ET.fromstring(response.content)

    result = xml.find('result')

    urls = map(lambda uid: "https://krameriusadmin.mzk.cz/search/i.jsp?pid="+(uid.findtext('str')), result.findall('doc'))

    for url in urls:
        print(url)


else:
    print("Chyba", response.status_code)