import socket               # Import socket module
import json

#functions
def Remove(x):  
    final_list2 = []
    for num in x: 
        if num not in final_list2: 
            final_list2.append(num) 
    return final_list2

def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated


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
   length=length-1
   n_d=r_d[1:length]
   print("numbers received as a string")
   print n_d
   print("\n")
   n_l = [int(k) for k in n_d.split(',')]
   print("converting strings into integers as integers")
   print n_l
   print("\n")
   r_r=[]
   o_r=[]
   r_r=Repeat(n_l)
   o_r=Remove(n_l)
   print("printing duplicates")
   print r_r
   print("\n")
   print("printing deduplicated list")
   print o_r
   print("\n")
c.close()                # Close the connection
   