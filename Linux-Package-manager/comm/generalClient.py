#!/usr/bin/env python

import socket
import os
import glob
import time

command = "hello"
flag = False

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to client
s.connect(('10.0.0.2', 2018))
print("Connection successful!")

if(command == "hello"):
	print("Command issued!")
	s.send((command).encode('utf-8'))
	s.close()

#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.0.0.2', 2018))
s.listen(1)
print("Waiting for response from server")
while(True):
	#accepting connection from client
	clientsocket, addr = serversocket.accept()
	print("Accepting connection!")
	for i in range(1):
		transfer = clientsocket.recv(5000)
	clientsocket.close()
	serversocket.close()
	break	
s.close()	
