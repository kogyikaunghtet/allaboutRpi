import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
try:
        while 1:
                GPIO.output(26, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(26, GPIO.LOW)
                time.sleep(0.5)
except:
        GPIO.cleanup()

