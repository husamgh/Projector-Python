#https://stackoverflow.com/questions/29554137/send-hexadecimal-string-to-socket-using-python

#import socket

#HOST = '169.254.1.12' 
#PORT = 7142
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT))
#DATA =(b'\x02\x00\x00\x00\x00\x02')

#s.send(DATA)
#data = s.recv(4096)
#s.close()
#print ('Received', repr(s))

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('169.254.170.65', 7142))
#s.sendall(bytes.fromhex('02 00 00 00 00 02')) #turn the projector on
s.sendall(bytes.fromhex('02 01 00 00 00 03')) #turn the projector off
data = s.recv(5000)
s.close()
print ('the projector is activated', repr(data))