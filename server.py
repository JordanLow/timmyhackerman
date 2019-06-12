import socket
import os

port = int(os.environ.get("PORT", 8081))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',port))

sock.listen(5)

while True:
    clientsock, address = sock.accept()
    print(f"Connection from {address} has been established")
    message = clientsocket.recv(9999)
    print(message.decode("utf-8"))
