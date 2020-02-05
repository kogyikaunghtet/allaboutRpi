import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trig,GPIO.LOW)

try:
    while 1:
       GPIO.output(trig,GPIO.HIGH)
       time.sleep(0.00001)
       GPIO.output(trig,GPIO.LOW)

       while GPIO.input(echo)==0:
          pulse_start = time.time()
       while GPIO.input(echo)==1:
          pulse_end = time.time()

       pulse_duration = pulse_end - pulse_start
       distance = pulse_duration * 17150
       distance = round(distance, 2)
       print "Distance:",distance,"cm"
       time.sleep(0.5)

except KeyboardInterrupt:
     GPIO.cleanup()
