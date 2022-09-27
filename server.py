import socket

host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:

    soc.bind((host, port))
    soc.listen()
    ketnoi, diachi = soc.accept()
    with ketnoi:
        print('Da ket noi voi: ', diachi)
        while True:
            data = ketnoi.recv(1024)
            if not data:
                break
            ketnoi.sendall(data)
            
            

    """bind() is used to associate the socket with a specific network interface and port number
    value passed in depend on the address family of the socket,
    in this one is socket.AF_INET(IPv4) so it expect a tuple (host, port)"""