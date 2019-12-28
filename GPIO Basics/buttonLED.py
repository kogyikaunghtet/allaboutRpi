import wiringpi
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode (2, 1)
wiringpi.pinMode (3, 0)
while 1:
        button = wiringpi.digitalRead (3)
        if button == 0:
                    wiringpi.digitalWrite (2, 1)
                    print "LED is ON!"
        else:
                    wiringpi.digitalWrite (2, 0)
                    print "LED is OFF!"

