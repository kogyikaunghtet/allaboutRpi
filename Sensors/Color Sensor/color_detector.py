import RPi.GPIO as GPIO
import time
s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10
def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")

def loop():
  temp = 1
  while(1):
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    red  = NUM_CYCLES / duration
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration

    if green<7000 and blue<9000 and red>11000:
      print("red")
      temp=1
    elif red<14000 and  blue>13000 and green<14000 and green>13000:
      print("green")
      temp=1
    elif green>15000 and red<11500 and blue>23000:
      print("blue")
      temp=1
    elif red<10000 and green<9000 and blue<10000 and temp==1:
      print("place the object.....")
      temp=0

def endprogram():
    GPIO.cleanup()
if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
	endprogram()
