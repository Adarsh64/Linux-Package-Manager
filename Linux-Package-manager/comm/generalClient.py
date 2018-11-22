#!/usr/bin/env python

import socket
import os
import glob
import time
from subprocess import call

command = "hello"
flag = False

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to client
s.connect(('10.0.0.2', 2018))
print("Connection successful!")
while(True):
	if(command == "hello"):
		print("Command issued!")
		s.send((command).encode('utf-8'))
		#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('10.0.0.1', 2018))
		s.listen(1)
		print("Waiting for response from server")
		flag = True
		while(flag):
			#accepting connection from client
			clientsocket, addr = serversocket.accept()
			print("Accepting connection!")
			for i in range(len(arr)):
				transfer = clientsocket.recv(5000)
			clientsocket.close()
			flag = False

	#for downloading ::: already done
	#for installing
	if("install" in command):
		s.send((command).encode('utf-8'))
		s.bind(('10.0.0.1', 2018))
		s.listen(1)
		clientsocket, addr = serversocket.accept()
		cmd = clientsocket.recv(5000)
		#save file and folder depends on command sent
#s.close()
