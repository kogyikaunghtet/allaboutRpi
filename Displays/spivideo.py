import sys
import os.path
import PIL
from luma.core.interface.serial import spi
from luma.oled.device import ssd1351
from luma.core.render import canvas
serial = spi(device=0, port=0)
import av
def main():
    video_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'images', 'movie.mp4'))
    print('Loading {}...'.format(video_path))
    clip = av.open(video_path)
    for frame in clip.decode(video=0):
        print('{} ------'.format(frame.index))
        img = frame.to_image()
        if img.width != device.width or img.height != device.height:
            size = device.width, device.height
            img = img.resize(size, PIL.Image.ANTIALIAS)
        device.display(img.convert(device.mode))

if __name__ == "__main__":
    try:
	device = ssd1351(serial, width=128, height=128)
        main()
    except KeyboardInterrupt:
        pass
