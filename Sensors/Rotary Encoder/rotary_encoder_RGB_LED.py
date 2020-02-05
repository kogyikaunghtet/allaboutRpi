from RPi import GPIO
from time import sleep
clk = 17
dt = 18
sw = 27
red = 13
green = 19
blue = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN)
GPIO.setup(dt, GPIO.IN)
GPIO.setup(sw, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
redPWM = GPIO.PWM(red, 1000)
greenPWM = GPIO.PWM(green, 1000)
bluePWM = GPIO.PWM(blue, 1000)
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)
counter = 0
clkLastState = GPIO.input(clk)
flag = 0
i = 0
try:
    while 1:
	switch = GPIO.input(sw)
	if switch == 0 and flag == 0:
	    i += 1
	    if i == 4:
		i = 1
	    flag = 1
	elif switch == 1:
	    flag = 0
	if i == 1:
            clkState = GPIO.input(clk)
            dtState = GPIO.input(dt)
            if clkState != clkLastState:
                if dtState != clkState:
                    counter += 1
		    if counter > 100:
			counter = 100
                else:
                    counter -= 1
		    if counter < 0:
			counter = 0
		redPWM.ChangeDutyCycle(counter)
                print "Red LED Duty Cycle",counter
            clkLastState = clkState
            sleep(0.001)
        if i == 2:
            clkState = GPIO.input(clk)
            dtState = GPIO.input(dt)
            if clkState != clkLastState:
                if dtState != clkState:
                    counter += 1
                    if counter > 100:
                        counter = 100
                else:
                    counter -= 1
                    if counter < 0:
                        counter = 0
                greenPWM.ChangeDutyCycle(counter)
                print counter
            clkLastState = clkState
            sleep(0.001)
        if i == 3:
            clkState = GPIO.input(clk)
            dtState = GPIO.input(dt)
            if clkState != clkLastState:
                if dtState != clkState:
                    counter += 1
                    if counter > 100:
                        counter = 100
                else:
                    counter -= 1
                    if counter < 0:
                        counter = 0
                bluePWM.ChangeDutyCycle(counter)
                print counter
            clkLastState = clkState
            sleep(0.001)
finally:
    GPIO.cleanup()
