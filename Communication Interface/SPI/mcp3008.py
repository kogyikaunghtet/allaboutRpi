import spidev
#from numpy import interp
import time
spi = spidev.SpiDev()
spi.open(0,0)

def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while 1:
        output = analogInput(0)
        #output = interp(output, [0, 1023], [0, 100])
        print 'Analog Value: ', output
        time.sleep(0.1)
