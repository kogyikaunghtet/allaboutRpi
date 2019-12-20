import bluetooth
server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )
port = 0x1001
server_sock.bind(("",port))
server_sock.listen(1)
client_sock,address = server_sock.accept()
print "Accepted connection from ",address
data = client_sock.recv(1024)
print "received [%s]" % data
client_sock.close()
server_sock.close()
