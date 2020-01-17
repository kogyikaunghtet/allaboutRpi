from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27)
while 1:
	lcd.cursor_pos = (0, 0)
	lcd.write_string(u'Kaung Htet Htun')
	lcd.cursor_pos = (1, 0)
	lcd.write_string(u'Phoewa Science')
	time.sleep(2)
	lcd.clear()
        lcd.cursor_pos = (1, 0)
        lcd.write_string(u'Kaung Htet Htun')
        lcd.cursor_pos = (0, 0)
        lcd.write_string(u'Phoewa Science')
	time.sleep(2)
	lcd.clear()
