import bluetooth
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",bluetooth.PORT_ANY))
server_sock.listen(1)
bluetooth.advertise_service(server_sock, "helloService",service_classes= [bluetooth.SERIAL_PORT_CLASS],profiles=[bluetooth.SERIAL_PORT_PROFILE])
client_sock, address = server_sock.accept()
print "Accepted connection from ",address
data = client_sock.recv(1024)
print "received [%s]" % data
client_sock.close()
server_sock.close()
