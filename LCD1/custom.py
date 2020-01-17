import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False)
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)
lcd.clear()
heart = (
	0b00000,
	0b01010,
	0b11111,
	0b11111,
	0b11111,
	0b01110,
	0b00100,
	0b00000
)
lcd.cursor_pos = (0, 0)
lcd.write_string(u'I')
lcd.create_char(0, heart)
lcd.write_string(unichr(0))
lcd.cursor_pos = (1, 2)
lcd.write_string(u'Raspberry Pi')
