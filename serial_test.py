# Importing Libraries
import serial
import time
import json

arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    start_sending = input("type anything for sending data") # start sending data
    data = {"connection_mode": "config","ssid": "NGT", "password": "11215Mnb", "mqtt_ip": "", "mqtt_username": "", "mqtt_password": "", "LB": "", "SignalBandwidth": "", "SpreadingFactor": "", "SyncWord": "", "CodingRate4": "", "TxPower": "", "Gain": ""}
    json_data = json.dumps(data)
    value = write_read(json_data)
    print(value) # printing the value