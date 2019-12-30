import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
        edge = GPIO.wait_for_edge(24, GPIO.FALLING, timeout=5000)
        if edge is None:
                print "Timeout occurred"
        else:
                print "Edge detected!"
except:
        GPIO.cleanup()
