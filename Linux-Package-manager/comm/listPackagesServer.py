#!/usr/bin/env python

import socket
import os
import glob
import time
packages = os.listdir("../Packages")
#print(packages)

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to client
s.connect(('10.0.0.2', 2018))
print("Connection successful!")
for i in packages:
	path = "../Packages/"+i
	info = os.stat(path)
	#print(info.st_size)
	package_size = str(info.st_size)
	find_version = os.listdir(path)
	find_version = find_version[0].split(sep = "-")
	version_number = str(find_version[-1])
	version_number = version_number.replace(".tgz", "")
	print(i+","+package_size+","+version_number+";")
	s.send((i+","+package_size+","+version_number+";").encode('utf-8'))
s.close()
print("Connection Closed!")
