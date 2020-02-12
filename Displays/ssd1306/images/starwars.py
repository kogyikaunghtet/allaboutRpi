from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
from PIL import Image
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=32)

while 1:
  photo = Image.open("starwars.png").transform((device.width, device.height), Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR)\
          .convert(device.mode)
  device.display(photo)
