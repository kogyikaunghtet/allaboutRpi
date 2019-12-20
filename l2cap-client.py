import bluetooth
sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
bd_addr = "C0:F8:DA:F5:7D:1D"
port = 0x1001
sock.connect((bd_addr, port))
sock.send("hello!!")
sock.close()
