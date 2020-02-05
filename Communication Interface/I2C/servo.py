import time
import smbus
from PCA9685 import PWM
bus = smbus.SMBus(1)
channel = 0
frequency = 50
address = 0x40
pwm = PWM(bus, address)
pwm.setFreq(frequency)
pwm.setDuty(channel,2)
time.sleep(3)
while 1:
    for i in range (2,13,1):
        pwm.setDuty(channel, i)
        time.sleep(0.3)
    for i in range (12,1,-1):
        pwm.setDuty(channel, i)
        time.sleep(0.3)
