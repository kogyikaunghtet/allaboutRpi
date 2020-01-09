from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]
password = ["1","2","3","4"]
inputkey = [None] *4
i = 0
ROW_PINS = [5,6,13,19]
COL_PINS = [26,21,20,16]
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
def printKey(key):
  global i
  print key
  inputkey [i] = key
  i += 1
  if i==4:
    if inputkey [0] == password [0] and inputkey [1] == password [1] and inputkey [2] == password [2] and inputkey [3] == password [3]:
      GPIO.output (17, GPIO.HIGH)
      i = 0
    else:
      print "Wrong Password. Try Again!"
      i = 0

keypad.registerKeyPressHandler(printKey)
try:
  while 1:
    time.sleep(0.2)
except:
  keypad.cleanup()
