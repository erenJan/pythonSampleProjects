import requests
import json
import os
import time 
from plyer import notification

#here is the free link of api https://covid-193.p.rapidapi.com/statistics
url = "https://covid-193.p.rapidapi.com/statistics"
#here is the rapi api key and host section
#sign up rapiapi and get ur api key for free
headers = {
    'x-rapidapi-key': "write your api key here",
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
new = response['response'][0]['cases']['new']
today_deaths = response['response'][0]['deaths']['new']
total_deaths = response['response'][0]['deaths']['total']
img_path = os.path.join("resources", "corona.ico")

while(True):
    notification.notify(
        title = "COVID19 Stats",
        message = "Today cases : {new_case}\nToday deaths : {new_deaths}\nActive cases : {active}\nTotal deaths : {total_deaths}\nTotal recovered : {recovered}".format(
            new_case = new,
            new_deaths = today_deaths,
            active = active,
            total_deaths = total_deaths,
            recovered = recovered
        ),  
        app_icon = img_path,
        timeout  = 60
    )
    time.sleep(60*60*12)

