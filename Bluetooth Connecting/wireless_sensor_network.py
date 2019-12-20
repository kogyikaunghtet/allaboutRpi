import bluetooth
import time
from time import sleep
bt_addr = "00:21:13:04:7D:8F"
port = 1
server_socket=bluetooth.BluetoothSocket (bluetooth.RFCOMM)
server_socket.connect((bt_addr,port))
data=""
while 1:
         value = open("sensor_value.txt","a")
         hour = time.strftime("%H")
         hour = int(hour)
         minute = time.strftime("%M")
         minute = int(minute)
         second = time.strftime("%S")
         second = int(second)
         timeString = '%s%d%s%d%s%d'%('Hour: ',hour,' Minute: ',minute, ' Second: ',second)
         data = server_socket.recv(1024)
         data_end = data.find('\n')
         database_store =  '%s%s%s\n'%(timeString, ' Received data: ', data)
         print database_store
         value.write (database_store)
         sleep(1)
         value.close()
server_socket.close()

