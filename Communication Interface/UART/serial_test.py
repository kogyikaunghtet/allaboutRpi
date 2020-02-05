import serial
port = serial.Serial('/dev/ttyS0', 9600, timeout=1)
data = raw_input("Say Something: ")
port.write(data)
rcv = port.read(10)
print rcv

