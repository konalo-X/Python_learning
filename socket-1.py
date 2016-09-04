import socket
socket.setdefaulttimeout(5)
s=socket.socket()
s.connect(('112.80.248.73',80))
ans =s.recv(2048)

