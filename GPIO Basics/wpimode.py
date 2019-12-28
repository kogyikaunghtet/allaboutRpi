import wiringpi
from time import sleep
wiringpi.wiringPiSetup()
wiringpi.pinMode(25,1)
try:
        while 1:
                wiringpi.digitalWrite(25, 1)
                sleep(0.5)
                wiringpi.digitalWrite(25, 0)
                sleep(0.5)
except:
        wiringpi.digitalWrite(25, 0)
	wiringpi.pinMode(25,0)

