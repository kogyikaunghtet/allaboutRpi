#!/usr/bin/env python
import RPi.GPIO as GPIO
import cgi
import cgitb; cgitb.enable()
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.HIGH)
print 'Status: 204 No Content'
print 'Content-type: text/plain\n'
print ''
