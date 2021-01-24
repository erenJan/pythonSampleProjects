import requests
import json
import time 
import pync

#here is the free link of api https://covid-193.p.rapidapi.com/statistics
url = "https://covid-193.p.rapidapi.com/statistics"
#here is the rapi api key and host section
#sign up rapiapi and get ur api key for free
headers = {
    'x-rapidapi-key': "60ab51196bmsh7870bbd7d4ac2c2p1f4a6ajsnffd540113285",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
#write the country which wants to know about it 
querystring = {
    "country":"turkey"
    }
#it return json formatted response
response = requests.request("GET", url, headers=headers, params = querystring)
response = json.loads(response.text)

date = response['response'][0]['day']
active = response['response'][0]['cases']['active']
recovered = response['response'][0]['cases']['recovered']
new = response['response'][0]['deaths']['new']

while(True):
        notification(
            "dlkfsdfklsdşfsdkl"
        )
        time.sleep(60)

