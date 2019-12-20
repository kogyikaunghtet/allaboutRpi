import bluetooth
bd_addr = "C0:F8:DA:F5:7D:1D"
port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
sock.send("hello!!")
sock.close()
