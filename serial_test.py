# Importing Libraries
import serial
import time
import json

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    data = {"hi": "world!"}
    json_data = json.dumps(data)
    value = write_read(json_data)
    print(value) # printing the value