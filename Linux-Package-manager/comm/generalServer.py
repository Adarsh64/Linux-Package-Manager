#!/usr/bin/env python

import socket
import os
import glob
import time

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.0.0.2', 2018))
s.listen(1)

flag = True
command = "online"
print("Waiting for command!")
while(flag):
	time.sleep(2)
	#accepting connection from client
	clientsocket, addr = s.accept()
	print("Message received!")
	command = (clientsocket.recv(5000)).decode('utf-8')
	if(command == "hello"):
		print("Listing command executed!")
		packages = os.listdir("../Packages")
		for i in packages:
			path = "../Packages/"+i
			info = os.stat(path)
			#print(info.st_size)
			#package_size = str(info.st_size)
			package_size = os.path.getsize(path)
			find_version = os.listdir(path)
			find_version = find_version[0].split(sep = "-")
			version_number = str(find_version[-1])
			version_number = version_number.replace(".tgz", "")
			print(i+","+package_size+","+version_number+";")
			s.send((i+","+package_size+","+version_number+";").encode('utf-8'))
		clientsocket.close()
	elif("download " in command):
		cmd = command.split(sep = " ")
		packages = os.listdir("../Packages")
		#cmd[1] gives package name
		for fzip in packages:
			if(cmd[1] in fzip):
				s.send(("../Packages/"+fzip).encode('utf-8'))
		clientsocket.close()
				break;
	elif(command == "stop"):
		clientsocket.close()
		s.close()
		break;
	else:
		clientsocket.close()
		print("Command not defined!")
