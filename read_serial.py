import json
import time
import serial

# Specify the COM port number
com_port = 'COM6'

# Configure the serial port
port = serial.Serial(com_port, baudrate=115200)

# Read all messages from the serial port
while True:
    try:
        message = {"cn_m": "pin_status"}
        port.write((json.dumps(message) + "\n").encode())
        time.sleep(1)
        # Read a line from the serial port
        line = port.readline().decode().strip()
        print(line)
        time.sleep(3)

    except KeyboardInterrupt:
        # Close the serial port and exit the program
        port.close()
        break
