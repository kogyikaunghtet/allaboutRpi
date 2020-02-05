import serial
port = serial.Serial('/dev/ttyS0', 9600, timeout=1)
while 1:
    data = raw_input("Send Character to Arduino: ")
    port.write(data)

