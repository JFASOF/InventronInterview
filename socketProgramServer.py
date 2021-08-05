import socket
import time

host = '127.0.0.1'
port = 8000
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))
msg = s.recv(1024)
while msg:
    time.sleep(20)
    s.send(str(time.timezone))
    print('Received:' + msg.decode())
    msg = s.recv(1024)
 
s.close()