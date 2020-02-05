import spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000

data = "Hello World\r"
datalist = list()
datalist = []

i=0
for x in data:
        datalist.insert(i,ord(x))
        i += 1

str(spi.xfer2(datalist))
spi.close()
