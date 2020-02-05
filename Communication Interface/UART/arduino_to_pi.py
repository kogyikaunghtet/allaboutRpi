import serial
port = serial.Serial('/dev/ttyS0', 9600, timeout=1)
while 1:
    if(port.in_waiting >0):
        line = port.readline()
        print(line)

