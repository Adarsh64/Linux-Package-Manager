#!/usr/bin/env python

import socket
import os
import glob
import time
#creating socket
packages = [f for f in glob.glob("../Packages")]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to client
s.connect(('192.168.0.102', 2018))
serversocket.listen(1)
print("Connection successful!")
for i in packages:
    info = os.stat(i)
    package_size = info.st_size >> 20
    find_version = os.listdir(i)
    find_version = find_version[0].split(sep = "-")
    version_number = find_version[-1]
    s.send(i+","+package_size+","+version_number+";")
s.close()
print("Connection Closed!")
