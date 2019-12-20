import bluetooth
from time import sleep
bt_addr = "00:21:13:04:7D:8F"
port = 1
server_socket=bluetooth.BluetoothSocket (bluetooth.RFCOMM)
server_socket.connect((bt_addr,port))
data=""
while 1:
         data = server_socket.recv(1024)
         data_end = data.find('\n')
         print data
         sleep(1)
server_socket.close()
