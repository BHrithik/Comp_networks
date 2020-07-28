####################################################################################
import os
import json
from socket import *
#######################
def Remove(duplicate): #function to remove duplicates from an array
    final_list = [] 
    for num in duplicate: 
        if num not in final_list:  
            final_list.append(num) 
    return final_list 
#################################
def AddDuplicateList(duplicate): # function to place duplicates in an array
    temp_list = []
    final_list = []
    for num in duplicate: 
        if num not in temp_list: 
            temp_list.append(num)
        else:
          if num not in final_list:
            final_list.append(num)
    return final_list 
#############################
def stringArrayToInt(array): #function to convert a string to an array of integers
        length = len(array)
        final_array = []
        temp_number=0
        iterator=0
        while(iterator in range(0,length)):
            while(array[iterator].isdigit()):
                temp_number = 10*temp_number + int(array[iterator])
                iterator+=1
            if(temp_number>0):
                final_array.append(temp_number)
            temp_number=0
            iterator+=1

        return final_array
############################
def intArrayToString(array): #function to convert an integer array to a string
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
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
while(True):
    print ("WAITING FOR INPUT")
    (data, addr) = UDPSock.recvfrom(buf)
    if(data == "exit"):
        print("server terminated")
        break
    int_data = stringArrayToInt(data)
    print("DATA RECIEVED:") 
    print(int_data)
    data = ('RESPONSE FROM SERVER:\nmodified data:\n'+intArrayToString(Remove(int_data))+'\nrepeating elements:\n'+intArrayToString(AddDuplicateList(int_data))+'\n\n')
    UDPSock.sendto(data,addr)
(data, addr) = UDPSock.recvfrom(buf)
print("MESSAGE FROM CLIENT:")
print(data)
UDPSock.close()
os._exit(0)
####################################################################################

#coded by Piyush 17-534