import requests
import json
import time
import datetime

# Api address
url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
# Calling from Api. Queryng only the wanted stuff.
# HSL id 113 facing kontula, 114 for mellunmäki
payload = {"query":"{\n  stop(id: \"HSL:1472113\") {  name   stoptimesWithoutPatterns{ scheduledArrival   scheduledDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
headers= {"Content-Type" : "application/json"}
response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
# Dumping the payload in json format
dumped_data = response.json()

""" print(response.text)
print(response.status_code) """

# Getting into the right places
# Fix naming conventions into singular
datawrap = dumped_data['data']
stopwrap = datawrap['stop']
stoptimes_wrap = stopwrap['stoptimesWithoutPatterns']
stop_name = stopwrap['name']

# Getting the bus sign from the dictionary
tripWrap = stoptimes_wrap[0]['trip']
routeWrap = tripWrap['route']
busRouteSign = routeWrap['shortName']
busHeadSign = stoptimes_wrap[0]['headsign']
# For testing if i get the right values
print(stop_name)
print(busRouteSign)
print(busHeadSign)
# print(stoptimes_wrap[1]['serviceDay'])
# print(stoptimes_wrap[2]['scheduledArrival'])

# Getting the next incoming bus time in utc
# Its holding the values inside. So doing[1] will give the next busses time
stopDay = int(stoptimes_wrap[0]['serviceDay'])
stopTime= int(stoptimes_wrap[0]['scheduledArrival'])
busTime = stopDay + stopTime
#print(busTime)
strBusTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(busTime))
print(strBusTime)
# Minutes Left
currentTime = time.time()
timeLeft = busTime - currentTime
#print (timeLeft)
if timeLeft <= 60:
    normLeft = "~0"
else:    
    normLeft = time.strftime('%M', time.localtime(timeLeft))
print(normLeft + " Minutes Left")