import wiringpi
from time import sleep
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(26,1)
try:
        while 1:
                wiringpi.digitalWrite(26, 1)
                sleep(0.5)
                wiringpi.digitalWrite(26, 0)
                sleep(0.5)
except:
        wiringpi.digitalWrite(26, 0)
	wiringpi.pinMode(26,0)

