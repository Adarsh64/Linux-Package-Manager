import sys
import os
#print ('Number of arguments: ',len(sys.argv))
File = sys.argv[1]
#print type(File)
#print (File)
port = 2017
'''K = os.listdir ("./packages")
#print (K)
if File in K:
	print ("Package exists!")
else:
	print ("Package does not exist!")'''
import socket
import time
#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s2 = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# connecting to server
s.connect(('192.168.43.15', port)) # give your system ip address and select port number
# 172.16.6.1 is the server IP address 8888 is the port number shared
# sending 10 packets with 2 seconds gap
s.send((File).encode('utf-8'))
#print "File sent to server"
s.close()


#Now, this becomes server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.43.15',port+1))
serversocket.listen(1)
while True:
# accepting connection from client
	clientsocket, addr = serversocket.accept()
	#print "Connected to server"
	# receiving 10 packets
	F = open(' curl-7.62.0.tar.gz','wb')
	for i in range(100):
		m = clientsocket.recv(404520)
		print (len(m))
		F.write(m)
		#print "-"*50
		#print "Response received from server"
		# receive only 50 at a time
	clientsocket.close()
	serversocket.close()
	#print m+" accessible outside the loop"
	break

