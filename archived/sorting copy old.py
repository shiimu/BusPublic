from webApp import dumped_data
import time

data_wrap = dumped_data['data']
stop_wrap = data_wrap['stop']
stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
stop_name = stop_wrap['name']

# Getting the bus sign.
trip_wrap = stop_times_wrap[0]['trip']
route_wrap = trip_wrap['route']
short_name_wrap = route_wrap['shortName']
# Getting the arrival time
stopDay = int(stop_times_wrap[0]['serviceDay'])
stopTime= int(stop_times_wrap[0]['realtimeArrival'])
busTime = stopDay + stopTime
# At first I had all 3 together. But had trouble singleing out any one var. so decided to split to 3 functions.
def busName(number):
    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def busTimeL(number):
    global norm_left

    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['realtimeArrival'])
    
    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - current_time
    # throws an error if time_left is negative
    if time_left <= 60:
        norm_left = "~0"
    else:    
        norm_left = time.strftime('%M', time.localtime(time_left)) 
        return norm_left
def busNumber(number):
    global bus_num

    bus_num = stop_times_wrap[number]['trip']['route']['shortName']

    return bus_num
    



#print(bus(0))