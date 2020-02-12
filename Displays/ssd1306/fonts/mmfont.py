from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import unicodedata
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=32)
#text.encode('utf8')
#mm = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
while 1:
    font_path = ('Pyidaungsu.ttf')
    myfont = ImageFont.truetype(font_path, 15)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white")
#        draw.text((5, 2),'\xff\xfe\x00\x101\x10,\x10\x04\x10:\x108\x10\x11\x10\x00\x10:\x10\x11\x10=\x10\x14\x10:\x108\x10', \
#	font=myfont, fill="white")
	draw.text((5, 2),'\xe1\x80\x80\xe1\x80\x81', fill="white")
