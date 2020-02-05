import dht11
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(4)
while 1:
    result = instance.read()
    error = result.error_code
    if error == 0:
        print 'Temperature =',result.temperature,'C'
        print 'Humidity =',result.humidity,'%'
        time.sleep(1)
    else:
	print "Please Wait"
	time.sleep(1)
