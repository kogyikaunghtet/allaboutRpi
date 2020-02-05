from RPi import GPIO
from time import sleep
clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN)
GPIO.setup(dt, GPIO.IN)
counter = 0
clkLastState = GPIO.input(clk)
try:
    while 1:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
            print counter
        clkLastState = clkState
        sleep(0.001)
finally:
    GPIO.cleanup()
