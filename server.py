import socket
import os

port = int(os.environ.get("PORT", 8081))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',port))

print(socket.gethostbyname(socket.gethostname()), port)

sock.listen(5)

while True:
    clientsock, address = sock.accept()
    print(f"Connection from {address} has been established")
    try:
        data = clientsock.recv(1024).decode('utf-8')
        
        if not data: 
            break

        print("Client Says: "+ data)
        clientsock.sendall("Server Says: Hi")
