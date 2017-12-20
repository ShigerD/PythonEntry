import socket
ipPort = ('127.0.0.1', 8888)
s = socket.socket()
host = socket.gethostname()
port = 8888
print host
s.connect(ipPort)
print s.recv(1024)
s.close()
