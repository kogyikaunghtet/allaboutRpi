import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24
red = 17
green = 27
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
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

       if distance < 10:
	  GPIO.output(red,GPIO.HIGH)
	  GPIO.output(green,GPIO.LOW)
       else:
	  GPIO.output(red,GPIO.LOW)
          GPIO.output(green,GPIO.HIGH)

except KeyboardInterrupt:
     GPIO.cleanup()
