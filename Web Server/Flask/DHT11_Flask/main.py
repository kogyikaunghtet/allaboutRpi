import dht11
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(4)

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
   result = instance.read()
   temperature = result.temperature
   humidity = result.humidity
   error = result.error_code
   templateData = {
      'temperature' : temperature,
      'humidity': humidity
       }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.0.150', port=80, debug=True)
