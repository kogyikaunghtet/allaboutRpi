import serial
import time
gsm = serial.Serial('/dev/ttyS0', 9600, timeout=1)

gsm.write('AT\r\n')
rcv = gsm.read(10)
print rcv
time.sleep(1)

gsm.write('ATE0\r\n')
rcv = gsm.read(10)
print rcv
time.sleep(1)

gsm.write('AT+CMGF=1\r\n')
rcv = gsm.read(10)
print rcv
time.sleep(1)

gsm.write('AT+CNMI=2,2,0,0,0\r\n')
rcv = gsm.read(10)
print rcv
time.sleep(1)

phone = raw_input("Enter Phone Number: ")
message = raw_input("Write SMS: ")
smscommand = 'AT+CMGS="' + phone + '\"'
time.sleep(1)
gsm.write(smscommand+'\r\n')
time.sleep(1)
gsm.write(message + '\r\n')
time.sleep(1)
gsm.write(chr(26))
time.sleep(2)

