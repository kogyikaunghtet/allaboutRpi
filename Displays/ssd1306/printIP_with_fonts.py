from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import os
import socket
import fcntl
import struct
from PIL import ImageFont
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=32)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

while 1:
#    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'FreePixel.ttf'))
#    myfont = ImageFont.truetype(font_path, 15)
    with canvas(device) as draw:
	myfont = ImageFont.truetype('fonts/FreePixel.ttf',15)
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((5, 2), "IP Address is", font=myfont, fill="white")
        draw.text((5, 15), get_ip_address('wlan0'), font=myfont, fill="white")
