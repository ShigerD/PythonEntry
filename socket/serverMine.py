import socket
ipPort = ('192.168.1.148', 8888)
s = socket.socket()
s.bind(ipPort)

s.listen(5) #max connect num
while True:
	c, addr = s.accept()
	print 'connect dir: ', addr 
	try:
		c.send('welcome to connect server')
	except Exception:
		break;
	c.close()
