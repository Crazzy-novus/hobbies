import socket

Host = socket.gethostname()
PORT = 9090
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,PORT))
for i in range(100):
    

    socket.send(f"Hello world!:{i}".encode('utf-8'))
    print(socket.recv(1024))
    