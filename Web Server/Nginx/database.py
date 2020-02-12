import MySQLdb
import dht11
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(4)
import time
db = MySQLdb.connect("localhost","kaung",\
"hello","sensor_data" )
cursor = db.cursor()
while 1:
    d = time.strftime("%m/%d/%Y")
    t = time.strftime("%H:%M:%S")
    result = instance.read()
    temp = result.temperature;
    humi = result.humidity;
    error = result.error_code
    if error == 0:
        sql = "INSERT INTO sensor_table(date,\
        time,temperature,humidity) VALUES ('%s', \
        '%s', '%d', '%d')" % (d, t, temp, humi)
	cursor.execute(sql)
	db.commit()
	time.sleep(2)
	print "done"
db.close()
