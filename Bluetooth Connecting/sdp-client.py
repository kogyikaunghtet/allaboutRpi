from bluetooth import *
services=find_service(name="helloService",uuid=SERIAL_PORT_CLASS)
for i in range(len(services)):
   match=services[i]
   if(match["name"]=="helloService"):
      port=match["port"]
      name=match["name"]
      host=match["host"]
      print name, port, host
      client_socket=BluetoothSocket( RFCOMM )
      client_socket.connect((host, port))
      client_socket.send("Hello world")
      client_socket.close()
      break
