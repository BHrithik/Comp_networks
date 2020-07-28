import socket               # Import socket module
import json
import random
#functions
def genrandarray(number,low,high):
	r=[]
	for x in range(number):
		r.append(random.randint(low,high))
	return r

#work
low=0
high=100
c=1
number=random.randint(25, 100)

#sockets

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name/for this example
	ports = 12345             #server port
	portc = 32451 	   #client's own port for incoming connections (if any)
	s.bind((host, portc))
	s.connect((host, ports))
	print s.recv(1024)
print("thank you for connecting")
s.close                     # Close the socket when done