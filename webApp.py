from flask import Flask, render_template, json, jsonify
import time
import requests
from callInfo import queryApi

app = Flask(__name__)

global stop_id
stop_id = 'HSL:1020453'
queryApi('HSL:1020453')
@app.route("/")
def bustimes():
    from sorting import data_wrap, refresh_data, bus_Number, bus_Name, bus_Time_Left
    refresh_data()
    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = bus_Number(0), busR1 = bus_Name(0), busT1 = bus_Time_Left(0),
                                                         busK2 = bus_Number(1), busR2 = bus_Name(1), busT2 = bus_Time_Left(1),
                                                         busK3 = bus_Number(2), busR3 = bus_Name(2), busT3 = bus_Time_Left(2),
                                                         busK4 = bus_Number(3), busR4 = bus_Name(3), busT4 = bus_Time_Left(3),
                                                         busK5 = bus_Number(4), busR5 = bus_Name(4), busT5 = bus_Time_Left(4)), queryApi(stop_id)
                                                                                                    

if __name__ == "__main__":
    app.run( debug = True )
