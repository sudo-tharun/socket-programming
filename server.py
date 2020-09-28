#file: server.py

import socket,pickle

HOST = "localhost"
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) #binding the port with the host address
s.listen(5) #putting in listening mode
(conn, addr) = s.accept() #accepting to receive a call from the sender
print ('Connected by', addr)
while 1:
    data = conn.recv(4096) #receiving the data from sender
    if not data: break
    data = pickle.loads(data) #loading the data from byte-stream
    print("Data Received: ",data,"\nCalculated sum: ",sum(data))
    data=sum(data)/len(data)
    print("Average sent to the client:", data)
    conn.send(str(data).encode()) #sending the response to the client
conn.close()