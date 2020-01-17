import RPi.GPIO as GPIO
import time
leftIR = 5
rightIR = 6
ENA = 18
IN1 = 12
IN2 = 16
IN3 = 20
IN4 = 21
ENB = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftIR,GPIO.IN)
GPIO.setup(rightIR,GPIO.IN)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
leftPWM = GPIO.PWM(ENA,1000)
rightPWM = GPIO.PWM(ENB,1000)
leftPWM.start(0)
rightPWM.start(0)
leftPWM.ChangeDutyCycle(100)
rightPWM.ChangeDutyCycle(100)
while 1:
    if(GPIO.input(leftIR)==0 and GPIO.input(rightIR)==0):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
	print "forward"
    elif(GPIO.input(leftIR)==1 and GPIO.input(rightIR)==0):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
	print "left"
    elif(GPIO.input(leftIR)==0 and GPIO.input(rightIR)==1):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.HIGH)
	print "right"
    else:
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)
	print "stop"
