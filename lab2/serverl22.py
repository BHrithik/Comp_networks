import socket               # Import socket module
import json
import random
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

def genrandarray(number,low,high):
  r=[]
  for x in range(number):
    r.append(random.randint(low,high))
  return r

def intersection(lst1, lst2):  
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    return lst3 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print 'host ip', host
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   r_d=[]
   print("working bro")
   while True:
    r_d.append(c.recv(1024))
    print("received element")
    if c.recv(1024)==10001:
      break
   length=len(r_d)
   print length
   length=length-1
   n_d=r_d[1:length]
   print("numbers received as a string")
   print n_d
   print("\n")
   n_l = [int(k) for k in n_d.split(',')]
   print("converting strings into integers")
   print n_l
   print("\n")
   length2=len(n_l)
   n_l2=[]
   n_l2=n_l[1:length2-2]
   if n_l[length2-1]==0:
      r_r=[]
      o_r=[]
      r_r=Repeat(n_l2)
      o_r=Remove(n_l2)
      print("printing duplicates")
      print r_r
      print("\n")
      print("printing deduplicated list")
      print o_r
      print("\n")
   if n_l[length2-1]==1 :
      cr=genrandarray(length2-1,0,100)
      print("new random array")
      print cr
      ir=[]
      ir=intersection(cr,n_l2)
      print("printing intersection")
      print ir
c.close()                # Close the connection
   