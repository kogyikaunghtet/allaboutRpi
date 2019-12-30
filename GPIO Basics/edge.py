import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
        while True:
                GPIO.wait_for_edge(24, GPIO.FALLING)
                print "Button Pressed"
                GPIO.wait_for_edge(24, GPIO.RISING)
                print "Button Released"
except:
        GPIO.cleanup()

