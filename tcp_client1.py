import socket

host = "192.168.1.179"
port = 4000
bufsize = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send("test")
sock.close()
pass
