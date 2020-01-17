import bluetooth
import time
import RPi.GPIO as GPIO
ENA = 18
IN1 = 12
IN2 = 16
IN3 = 20
IN4 = 21
ENB = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
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
leftPWM.ChangeDutyCycle(50)
rightPWM.ChangeDutyCycle(50)
bt_addr = "00:18:E4:40:00:06"
port = 1
server_socket=bluetooth.BluetoothSocket (bluetooth.RFCOMM)
server_socket.connect((bt_addr,port))
def right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
def left():
   GPIO.output(IN1,GPIO.LOW)
   GPIO.output(IN2,GPIO.HIGH)
   GPIO.output(IN3,GPIO.HIGH)
   GPIO.output(IN4,GPIO.LOW)
def forward():
   GPIO.output(IN1,GPIO.HIGH)
   GPIO.output(IN2,GPIO.LOW)
   GPIO.output(IN3,GPIO.HIGH)
   GPIO.output(IN4,GPIO.LOW)
def backward():
   GPIO.output(IN1,GPIO.LOW)
   GPIO.output(IN2,GPIO.HIGH)
   GPIO.output(IN3,GPIO.LOW)
   GPIO.output(IN4,GPIO.HIGH)
def stop():
   GPIO.output(IN1,GPIO.LOW)
   GPIO.output(IN2,GPIO.LOW)
   GPIO.output(IN3,GPIO.LOW)
   GPIO.output(IN4,GPIO.LOW)
data=""
while 1:
         data= server_socket.recv(1024)
	 data_end = data.find('\n')
         print "Received: %s" % data
         if (data == "F"):
            forward()
         elif (data == "L"):
            left()
         elif (data == "R"):
            right()
         elif (data == "B"):
            backward()
         elif data == "S":
            stop()
server_socket.close()
