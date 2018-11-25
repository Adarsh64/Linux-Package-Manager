import socket
import os
import time

# creating a socket to listen for incoming connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2017
serversocket.bind(('192.168.43.15',port))
serversocket.listen(1)
m = "init"
Extn = ".pdf"
while True:
# accepting connection from client
	clientsocket, addr = serversocket.accept()
	#print "Connected to client"
	# receiving 10 packets
	for i in range(1):
		m = clientsocket.recv(5000)
		#print (m)
		#print "-"*50
		#print "File received from client"
		# receive only 50 at a time
	clientsocket.close()
	serversocket.close()
	#print m+" accessible outside the loop"
	break
K = os.listdir ("./packages")
File = m.decode()
if File in K:
	#print "Package exists!"
	#Now, this becomes client
	#new client establishes connection
	F = open ('./packages/'+File,'rb')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.43.15', port+1))
	s.send(F.read())
	F.close()
	#print "File sent to server"
	s.close()

else:
	print ("Package does not exist!")
