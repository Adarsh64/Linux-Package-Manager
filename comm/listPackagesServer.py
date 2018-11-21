#!/usr/bin/env python

import socket
import os
import glob
import time
#creating socket
packages = [f for f in glob.glob("Packages")]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to client
s.connect(('192.168.0.102', 2018))
serversocket.listen(1)
print("Connection successful!")
s.send(packages)
print("File sent!")
s.close()
