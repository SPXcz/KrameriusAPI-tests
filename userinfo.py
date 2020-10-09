import json
import requests
from secrets.py import password

query = "http://krameriusadmin.mzk.cz/search/api/v5.0/user/"

response = requests.post(
            query,
            data={
                "user":""
                "pswd": ""
            },
        )

if response.status_code < 400:
    print(response.json())
else:
    print("Status code: ", response.status_code)