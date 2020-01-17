from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27)
lcd.cursor_pos = (0, 0)
lcd.write_string(u'Kaung Htet Htun')
lcd.cursor_pos = (1, 0)
lcd.write_string(u'Phoewa Science')
