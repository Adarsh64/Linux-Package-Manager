import sys
import os
#print ('Number of arguments: ',len(sys.argv))
File = sys.argv[1]
#print type(File)
#print (File)

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
s.connect(('10.0.0.1', 2018)) # give your system ip address and select port number
# 172.16.6.1 is the server IP address 8888 is the port number shared
# sending 10 packets with 2 seconds gap
s.send((File).encode('utf-8'))
#print "File sent to server"
s.close()


#Now, this becomes server
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.0.0.1',2019))
s.listen(1)
while True:
# accepting connection from client
	clientsocket, addr = serversocket.accept()
	#print "Connected to server"
	# receiving 10 packets
	F = open('download.pdf','wb')
	for i in range(100):
		m = clientsocket.recv(5000)
		#print (m)
		F.write(m)
		#print "-"*50
		#print "Response received from server"
		# receive only 50 at a time
	clientsocket.close()
	serversocket.close()
	#print m+" accessible outside the loop"
	break

