
import socket
host = '127.0.0.1'
port = 5000
  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
  
c, addr = s.accept()
print("CONNECTION FROM:", str(addr))
c.send("DATETIME")
 
msg = "Over.............."
c.send(msg.encode())

c.close()