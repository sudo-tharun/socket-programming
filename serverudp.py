#file: server.py

import socket,pickle

HOST = "localhost"
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT)) #binding the port with the host address
while 1:
    data = s.recvfrom(4096) #receiving the data from sender
    if not data: break
    #data = pickle.loads(data) #loading the data from byte-stream
    data_string=data[0]
    data_string=pickle.loads(data_string)
    data_address=data[1]
    print("Data Received: ",data_string,"\nCalculated sum: ",sum(data_string))
    data_string=sum(data_string)/len(data_string)
    print("Average sent to the client:", data_string)
    s.sendto(str(data_string).encode(),data_address) #sending the response to the client
s.close()