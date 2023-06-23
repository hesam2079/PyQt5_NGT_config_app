import serial

# Specify the COM port number
com_port = 'COM9'

# Configure the serial port
port = serial.Serial(com_port, baudrate=9600, timeout=1)

# Read all messages from the serial port
while True:
    try:
        # Read a line from the serial port
        line = port.readline().decode('utf-8').strip()

        # Check if the line is not empty
        if line:
            print(line)

    except KeyboardInterrupt:
        # Close the serial port and exit the program
        port.close()
        break
