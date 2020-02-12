from picamera import PiCamera, Color
from time import sleep
camera = PiCamera()
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
