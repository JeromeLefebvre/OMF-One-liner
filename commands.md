# Retrieve weather data
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "."


# Retrieve just the temperature and format it for OMF
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[ {containerid : .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}] }]"

[
  {
    "containerid": 1850147,
    "values": [
      {
        "time": "2020-12-02T00:25:53Z",
        "Temperature": 282.68
      }
    ]
  }
]

# push it to PIWA

curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[ {containerid : .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}] }]" | curl --location --request POST "https://localhost/piwebapi/omf" --header "messagetype:Data" --header "messageformat:JSON" --header "Content-Type:application/json" --header "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ==" --header "X-Requested-WIth:xmlhttprequest" --header "action:create" --data-binary @- --header "omfversion:1.1"


## Optimize pushing to PI WA
Working:
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl --location --request POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "messageformat:JSON" -H "Content-Type:application/json" -H "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ==" -H "action:create" -H "omfversion:1.1" --data-binary @-


Tweaking:
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl --location --request POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ==" -H "action:create" -H "omfversion:1.1" --data-binary @-

Further:
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ==" -H "action:create" -H "omfversion:1.1" --data-binary @-


curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ==" -H "action:create" -H "omfversion:1.1" --data-binary @-

** Attempting to use -negotiate

curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "omfversion:1.1" -d @- --negotiate -u :



curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime('%Y-%m-%dT%H:%M:%SZ')), Temperature: .main.temp}]}]" 

# push it to EDS


curl -H "Content-Type: application/json" -X POST -d -L '{"key1":"value1","key2":"value2"}' https://jlefebvre7390.osisoft.int/piwebapi/omf




### CURL in general

curl --location --request POST 'https://localhost/piwebapi/omf'
Problem
curl: (1) Protocol "'https" not supported or disabled in libcurl
Solution
Need double quotes


curl --location --request POST "https://localhost/piwebapi/omf" --header "messagetype:Data" --header "messageformat:JSON" --header "Content-Type:application/json" --data-raw "[{\"containerid\": \"1850147\",\"values\": [ {\"Time\": \"2020-11-24T03:37:19.000Z\",\"Temperature\": 99}]}]"
Problem
No answer
SOlution
Add auth




curl --location --request POST "https://localhost/piwebapi/omf" --header "messagetype:Data" --header "messageformat:JSON" --header "Content-Type:application/json" --header "Authorization: Basic ...==" --header "X-Requested-WIth:xmlhttprequest" --header "action:create" --data-raw "[{\"containerid\": \"1850147\",\"values\": [ {\"Time\": \"2020-11-24T03:37:19.000Z\",\"Temperature\": 99}]}]"
Not enough info in the error message:
・ｿ{
  "OperationId": "320e80a6-10bc-4942-8ec3-9eb05a67e812",
  "Messages": [
    {
      "MessageIndex": null,
      "Events": [
        {
          "EventInfo": {
            "Message": "OMF message does not contain required header.",
            "Reason": null,
            "Suggestions": [],
            "EventCode": 2001,
            "Parameters": []
          },
          "ExceptionInfo": null,
          "Severity": "Error",
          "InnerEvents": []
        }
      ],
      "Status": {
        "Code": 400,
        "HighestSeverity": "Error"
      }
    }
  ]
}
* Solution
Turn debugMode=True




curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[ {containerid : .id, values: [Ttime: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}] }]"


curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[ {containerid : .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}] }]"



curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "Authorization: Basic ...==" -H "action:create" -H "omfversion:1.1" --data-binary @-



curl "https://localhost/piwebapi" -H "Authorization: Basic b3NpXGpsZWZlYnZyZToyMDIwMTAwMUV2aWRlbmNlIQ=="

curl "https://localhost/piwebapi" -ntlm --negotiate -u

curl "https://localhost/piwebapi" --negotiate -u :


curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "omfversion:1.1" --data-binary @- --negotiate -u :




### DEMO
1. Retrieve weather data
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" | jq "."

2. Format it
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" | jq "[{containerid: .id, values: [{Time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]"


3. Send it
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "https://localhost/piwebapi/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "omfversion:1.1" -d @- --negotiate -u :

4. send it to EDS
curl "https://api.openweathermap.org/data/2.5/weather?id=1850147&APPID=33ed95774fd9f0308a9135bb8dd8a2c9&units=metric" | jq "[{containerid: .id, values: [{time: (.dt | strftime(\"%Y-%m-%dT%H:%M:%SZ\")), Temperature: .main.temp}]}]" | curl -X POST "http://localhost:5590/api/v1/tenants/default/namespaces/default/omf" -H "messagetype:Data" -H "Content-Type:application/json" -H "omfversion:1.1" -d @- -H "messageformat:JSON"
