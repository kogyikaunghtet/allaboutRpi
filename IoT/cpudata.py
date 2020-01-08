import httplib
import urllib
import time
API_key = "8ALM3YDAT2N4G16D"
while 1:
        cpu = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
        params = urllib.urlencode({'field1': cpu, 'key': API_key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print cpu
                print response.status, response.reason
                data = response.read()
                conn.close()
        except KeyboardInterrupt:
                break
