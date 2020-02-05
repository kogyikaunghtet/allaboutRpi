from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1351
import os.path
from PIL import Image
serial = spi(device=0, port=0)
device = ssd1351(serial)
while 1:
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")
    fff = Image.new(logo.mode, logo.size, (255,) * 4)
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)

    while True:
        for angle in range(0, 360, 2):
            rot = logo.rotate(angle, resample=Image.BILINEAR)
            img = Image.composite(rot, fff, rot)
            background.paste(img, posn)
            device.display(background.convert(device.mode))
