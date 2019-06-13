import socket
import os

port = int(os.environ.get("PORT", 8081))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0',port))

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
        
        try:
            req = data.split(' ')[1].split('?')[0].lstrip('/')
            
            if req == '/':
                req = 'index.html'
                file = open(myfile,'rb') # open file , r => read , b => byte format
                response = file.read()
                file.close()
                header = 'HTTP/1.1 200 OK\n'
                mimetype = 'text/html'
                header += 'Content-Type: '+str(mimetype)+'\n\n'
                final_response = header.encode('utf-8')
                final_response += response
                clientsock.send(final_response)
            except:
                print("Oops! Something went wrong!")
 
    except:
            print("Oops! Something went wrong!")
       
