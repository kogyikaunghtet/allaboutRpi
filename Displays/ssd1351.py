from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1351
import socket
import fcntl
import struct
serial = spi(device=0, port=0)
device = ssd1351(serial)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

while 1:
  with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="#1805b8")
    draw.text((25, 2), "IP Address is", fill="white")
    draw.text((25, 15), get_ip_address('wlan0'), fill="white")
