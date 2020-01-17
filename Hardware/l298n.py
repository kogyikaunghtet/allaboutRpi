import RPi.GPIO as GPIO
import time
ENA = 13
IN1 = 19
IN2 = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
PWM = GPIO.PWM(ENA,1000)
PWM.start(0)
while 1:
	GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
	PWM.ChangeDutyCycle(50)
	time.sleep(3)
	GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
	PWM.ChangeDutyCycle(100)
	time.sleep(3)

