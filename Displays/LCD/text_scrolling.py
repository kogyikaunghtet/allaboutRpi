from RPLCD.i2c import CharLCD
import time
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2, backlight_enabled=True)
framebuffer = [
    'Hello World',
    '',
]

def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

write_to_lcd(lcd, framebuffer, 16)
text = 'all about Raspberry Pi book'

def loop_string(text, lcd, framebuffer, row, num_cols, delay=0.1):
    blank_space = ' ' * 16
    s = blank_space + text + blank_space
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

while True:
    loop_string(text, lcd, framebuffer, 1, 16)
