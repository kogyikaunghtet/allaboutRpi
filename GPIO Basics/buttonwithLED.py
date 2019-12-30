import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.IN)
try:
   while 1:
      if GPIO.input(3) == 0:
         GPIO.output(2, GPIO.HIGH)
      else:
          GPIO.output(2, GPIO.LOW)
except:
   GPIO.cleanup()

