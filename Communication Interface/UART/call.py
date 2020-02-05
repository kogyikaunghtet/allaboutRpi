import serial
import time
gsm = serial.Serial('/dev/ttyS0',9600,timeout=1)
phone = raw_input("Enter Phone Number: ")
callcommand = 'ATD' + phone + ';'
gsm.write(callcommand+'\r')
gsm.write(chr(26))
time.sleep(10)
gsm.close()

