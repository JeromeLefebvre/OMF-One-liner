import os
import time

cities = [1850147,2063523]

requestTemplate  = r'curl "https://api.openweathermap.org/data/2.5/weather?id=CITYID&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "omfversion:1.1" -d @- --negotiate -u :'

requestWeatherOnly = r'curl "https://api.openweathermap.org/data/2.5/weather?id=CITYID&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" '
#requestTemplate  = r'curl "https://api.openweathermap.org/data/2.5/weather?id=CITYID&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" '

while True:
    for city in cities:
        request = requestTemplate.replace("CITYID", str(city))
        print("Fetching data for ", city)
        os.system(request)
        #os.system(requestWeatherOnly.replace("CITYID", str(city)))

    time.sleep(60*8)
