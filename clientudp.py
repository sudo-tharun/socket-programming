#file: client.py

import socket, pickle
#pickle to serialize the data

HOST = "localhost"
PORT = 5000
address=HOST,PORT
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
arr=list()
n=int(input("Enter the number of elements for which the average has to be calculated \n →"))
print("Enter the numbers: ")
for i in range(n):
    k=int(input("→ "))
    arr.append(k)
data_string = pickle.dumps(arr) #converting to byte stream
s.sendto(data_string,address) #sending data

data = s.recvfrom(4096) #receiving data from the server
s.close()
print ('Average of the list', arr,"is {}".format(data[0]))