#!/usr/bin/env python

import socket
import os
import glob
import time

# creating a socket to listen for incoming connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.0.0.2', 2018))
serversocket.listen(1)
package_list = []
while True:
	# accepting connection from client
	clientsocket, addr = serversocket.accept()
	print("Connection Successful!")
	for i in range(5):
		m = clientsocket.recv(500)
		package_list.append(m)
	clientsocket.close()
	#serversocket.close()

