import requests
import json
import time
import datetime


# Use HSL:(int) code here to query the right stop
def queryApi(stop_id):
    # Api address
    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    # Calling from Api. Queryng only the wanted stuff.
    payload = {"query":"{\n  stop(id: \"" + stop_id + "\") {  name   stoptimesWithoutPatterns{realtimeDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
    headers= {"Content-Type" : "application/json"}
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    # Dumping the response in json format
    global dumped_data
    dumped_data = response.json()
    #print(dumped_data)
    with open('datadump.json', 'w')as json_file:
        json.dump(dumped_data, json_file)
    return



