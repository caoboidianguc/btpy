import socket


host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((host, port))
    soc.sendall(b'hellooo there!')
    data = soc.recv(1024)
    
print('Nhan duoc tu client', repr(data))