import fauxmo
import logging
import time
import sys
import RPi.GPIO as GPIO
from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    #TRIGGERS = {str(sys.argv[1]): int(sys.argv[2])}
    #TRIGGERS = {"Light": 52000}
    TRIGGERS = {"office":52000}

    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        GPIO.setup(int(11), GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
        GPIO.output(int(11), state) ## State is true/false
        return True
 
if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)
 
    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)
 
    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception as e:
            logging.critical("Critical exception: "+ e.args  )
            break
