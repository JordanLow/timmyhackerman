import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',7859))

sock.listen(5)

while True:
    clientsock, address = sock.accept()
    print(f"Connection from {address} has been established")
    message = clientsocket.recv(9999)
    print(message.decode("utf-8"))
