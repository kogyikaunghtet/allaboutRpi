from RPLCD.i2c import CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2, auto_linebreaks=True, backlight_enabled=True)
lcd.write_string(u'Kaung Htet Htun Phoewa Science')
