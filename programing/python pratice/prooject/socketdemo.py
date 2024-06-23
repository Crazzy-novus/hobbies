import socket
import _thread
import sys

HOST = socket.gethostname()
PORT = 9090
#HOST  = '192.168.86.84'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(6)

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from clint is: {message}")
    communication_socket.send("got your message ! thank you".encode('utf-8'))
    
# 192.168.86.84