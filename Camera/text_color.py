from picamera import PiCamera, Color
from time import sleep
camera = PiCamera()
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
camera.annotate_text_size = 50
sleep(5)
camera.stop_preview()

