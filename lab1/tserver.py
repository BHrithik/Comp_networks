import socket               # Import socket module
import json
import os

####################################################################################
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
####################################################################################
def AddDuplicateList(duplicate):
    temp_list = []
    final_list = []
    for num in duplicate: 
        if num not in temp_list: 
            temp_list.append(num)
        else:
          if num not in final_list:
            final_list.append(num)
    return final_list 
####################################################################################    
def stringArrayToInt(array):
  length = len(array)
  final_array = []
  temp_number=0
  for iterator in range(0,length):
    if(array[iterator].isdigit()):
      temp_number = temp_number+int(array[iterator])
      iterator+=1
      if(array[iterator].isdigit()):
        temp_number = temp_number*10 + int(array[iterator])
        iterator+=1
        if(array[iterator].isdigit()):
          temp_number = temp_number*10 + int(array[iterator])
      if(temp_number !=0):
        final_array.append(int(temp_number))
      temp_number = 0
  return final_array
  ####################################################################################
def intArrayToString(array):
  string = ''
  length = len(array)
  string+=('[')
  for iterator in range(0,length-1):
    temp_string = str(array[iterator])
    string+=(temp_string)
    string+=(',')
    string+=(' ')
  string+=str(array[length-1])
  string+=(']')
  return string
####################################################################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)     # Create a socket object
host = socket.gethostbyname(socket.gethostname())            # Get local machine name
port = 12345                                                 # Reserve a port for your service.
s.bind((host, port))                                         # Bind to the port

print 'host ip', host
s.listen(5)                                                  # Now wait for client connection.
while True:
   c, addr = s.accept()                                      # Establish connection with client.
   print 'Got connection from', addr
   recieved_data = c.recv(1024)       
   int_data = stringArrayToInt(recieved_data)                       #print(recieved_data)
   c.send('recieved data:\n'+recieved_data+'\nmodified data:\n'+intArrayToString(Remove(int_data))+'\nrepeating elements:\n'+intArrayToString(AddDuplicateList(int_data))+'\n\n')
   recieved_data = c.recv(1024)  
   print(recieved_data)
   c.close()                                               # Close the connection
####################################################################################