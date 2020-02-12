from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1351
from PIL import ImageFont
import time
serial = spi(device=0, port=0)
device = ssd1351(serial)
with canvas(device) as draw:
  font_path = ('FreePixel.ttf')
  myfont = ImageFont.truetype(font_path, 15)
  draw.rectangle(device.bounding_box, outline="#08a211")
  draw.text((18, 10), "Hello World", font=myfont, fill="white")
  draw.text((5, 50), "Kaung Htet Htun", font=myfont, fill="#c411a9")
  draw.text((10, 70), "Phoewa Science", font=myfont, fill="#0477a9")
time.sleep(30)
