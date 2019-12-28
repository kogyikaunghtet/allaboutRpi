import wiringpi
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode (2, 0)
while 1:
        button = wiringpi.digitalRead (2)
        if button == 0:
                print "Button pressed"
        else:
                print "Button released"

