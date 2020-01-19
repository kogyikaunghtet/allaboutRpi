from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import socket
import fcntl
import struct
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
  with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((25, 2), "IP Address is", fill="white")
    draw.text((25, 15), get_ip_address('wlan0'), fill="white")
