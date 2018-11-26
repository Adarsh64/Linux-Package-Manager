#!/usr/bin/env python

import socket
import os
import glob
import time

#creating socket
port = 4015
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.43.15', port))
s.listen(1)

flag = True
command = "online"
print("Waiting for command!")
while(flag):
	#time.sleep(2)
	#accepting connection from client
	clientsocket, addr = s.accept()
	print("Message received!")
	command = clientsocket.recv(30).decode('utf-8')
	print('command ',command)
	if(command == "hello"):
		print("Listing command executed!")
		packages = os.listdir("../Packages")
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
			version_number = version_number.replace(".tgz", "")
			print(i+","+package_size+","+version_number+";")
			clientsocket.send((i+" " +package_size+" "+version_number+";").encode('utf-8'))
		clientsocket.close()
	elif("download " in command):
		cmd = command.split(sep = " ")
		packages = os.listdir("../Packages")
		#cmd[1] gives package name
		for fzip in packages:
			if(cmd[1] in fzip):
				path = os.listdir("../Packages/"+fzip)[0]
				print(path)
				f = open("../Packages/"+fzip+'/'+path,'rb')
				#print(f)
				#print(f.read())
				clientsocket.send(f.read())
				f.close()
				clientsocket.close()
				break
	elif("install" in command):
		cmd = command.split(sep = " ")
		scripts = os.listdir("../install")
		#cmd[1] gives package name
		for f in scripts:
			if(cmd[1] in f):
				f = open("../install/"+f,'rb')
				clientsocket.send((f.read()))
				clientsocket.close()
				print("install file sent")
				break
	elif(command == "stop"):
		clientsocket.close()
		s.close()
		break
	else:
		clientsocket.close()
		print("Command not defined!")
