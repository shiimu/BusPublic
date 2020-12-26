import requests
import json
import time
import datetime


# Use HSL:(int) code here to query the right stop
# Api address
url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
# Calling from Api. Queryng only the wanted stuff.
payload = {"query":"{nearest(lat: 60.239, lon: 25.10109, maxDistance: 500, filterByPlaceTypes: DEPARTURE_ROW) {  edges {      node {        place {  ...on DepartureRow {stop {lat lon name            }        stoptimes {              serviceDay              scheduledDeparture              realtimeDeparture              trip {                route {                  shortName                 longName                }              }              headsign            }          }        }      	distance      }    }}}}"}
headers= {"Content-Type" : "application/json"}
response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
# Dumping the response in json format
global dumped_data
dumped_data = response.json()
print(dumped_data)
#    with open('datadump.json', 'w')as json_file:
#        json.dump(dumped_data, json_file)
    



