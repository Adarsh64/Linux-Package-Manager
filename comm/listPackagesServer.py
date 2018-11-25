#!/usr/bin/env python

import socket
import os
import glob
import time
packages = os.listdir("../Packages")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to client
s.bind(('192.168.43.15',4001))
s.listen(1)
while True:
	clientsocket, addr = s.accept()
	print ("Connected to client")
	m = clientsocket.recv(5).decode()
	if m=="hello":
		for i in packages:
			path = "../Packages/"+i
			info = os.stat(path)
			#print(info.st_size)
			#package_size = str(info.st_size)
			find_version = os.listdir(path)
			package_size = str(os.path.getsize(path+"/"+str(find_version[0])))
			find_version = find_version[0].split(sep = "-")
			version_number = str(find_version[-1])
			version_number = version_number.replace(".tar.gz", "")
			print(i+","+package_size+","+version_number+";")
			clientsocket.send((i+" " +package_size+" "+version_number+";").encode('utf-8'))
		clientsocket.close()

		print("Connection Closed!")
s.close()
