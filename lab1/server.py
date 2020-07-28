import socket               # Import socket module
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print 'host ip', host
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   r_d=c.recv(1024)
   length=len(r_d)
   print length
   n_d=[]
   for x in range(1,length-1)
   		n_d[x-1]=r_d[x]
c.close()                # Close the connection
   