from pad4pi import rpi_gpio
import time
def print_key(key):
    print(key)
try:
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_4_by_4_keypad()
    keypad.registerKeyPressHandler(print_key)
    print("Press buttons on your keypad. Ctrl+C to exit.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Goodbye")
finally:
    keypad.cleanup()
