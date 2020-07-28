import socket               # Import socket module
import json
import random
#functions
def genrandarray(number,low,high,c):
	r=[]
	for x in range(number):
		r.append(random.randint(low,high))
	if c==1:
		r.append(0)
	if c==2:
		r.append(1)
	return r


#work
low=0
high=100
c=1
number=random.randint(25, 100)
while c==1:
	print("1-generate random numbers and deduplication ")
	print("2-generate random numbers and find intersection")
	print("3-quit")
	c=input()
	if c==1:
		ar = genrandarray(number,low,high,c)
	if c==2:
		ar = genrandarray(number,low,high,c)	
	if c==3:
		break
#sockets

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name/for this example
	ports = 12345             #server port
	portc = 32451 	   #client's own port for incoming connections (if any)
	s.bind((host, portc))
	s.connect((host, ports))
	length=len(ar)
	print("working bro")
	for x in xrange(0,length):
		print("sending element")
		d=json.dumps(ar[x])
		s.send(d.encode())
	s.recv(1024)
	done=10001
	s.send(done)
	print s.recv(1024)
s.Close                    # Close the socket when done