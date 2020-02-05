import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
reader = SimpleMFRC522()
print("Place your tag to read")
while 1:
	id, text = reader.read()
	print(id)
	print(text)
	if id == 255354276360:
		GPIO.output(17, GPIO.HIGH)
	else:
		GPIO.output(17, GPIO.LOW)
