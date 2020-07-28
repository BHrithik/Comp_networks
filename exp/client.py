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
while c==1:
	print("1-generate random numbers")
	print("2-quit")
	c=input()
	if c==1:
		ar = genrandarray(number,low,high)
	if c==2:
		break
#sockets

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name/for this example
	ports = 12345             #server port
	portc = 32451 	   #client's own port for incoming connections (if any)
	s.bind((host, portc))
	s.connect((host, ports))
	d=json.dumps(ar)
	s.send(d.encode())
	print s.recv(1024)

s.Close                    # Close the socket when done