#!/usr/bin/env python

import socket
import os
import glob
import time

# creating a socket to listen for incoming connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.0.0.2', 2018))
serversocket.listen(1)

while True:
	# accepting connection from client
	clientsocket, addr = serversocket.accept()
	print("Connection Successful!")
	for i in range(2):
		m = clientsocket.recv(5000)
		print (m)
	#clientsocket.close()
	#serversocket.close()

