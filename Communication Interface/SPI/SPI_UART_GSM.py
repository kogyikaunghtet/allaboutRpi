import spidev
import serial
import time
gsm = serial.Serial('/dev/ttyS0',9600,timeout=1)
spi = spidev.SpiDev()
spi.open(0,0)

def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while 1:
    ldr = analogInput(0)
    print 'LDR Value: ', ldr
    if ldr < 500:
        gsm.write('ATD0943158682;\r')
        gsm.write(chr(26))
        time.sleep(10)
