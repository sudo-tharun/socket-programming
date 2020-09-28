#file: client.py

import socket, pickle
#pickle to serialize the data

HOST = "localhost"
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) #establishing connection
arr=list()
n=int(input("Enter the number of elements for which the average has to be calculated \n →"))
print("Enter the numbers: ")
for i in range(n):
    k=int(input("→ "))
    arr.append(k)
data_string = pickle.dumps(arr) #converting to byte stream
s.send(data_string) #sending data

data = s.recv(4096) #receiving data from the server
data_arr = data.decode() #decoding data
s.close()
print ('Average of the list', arr,"is", data_arr)