from flask import *
import subprocess
import socket
import time
import os
import glob

app = Flask(__name__)

@app.route('/')
def home():
	packages = subprocess.getoutput('dpkg -l').split('\n')[5:]
	pip_packages = subprocess.getoutput('pip list').split('\n')[2:-2]
	for i in range(0,len(packages)):
		packages[i] = packages[i][3:].split()
		packages[i][3] = ' '.join(packages[i][3:])
		packages[i] = packages[i][0:4]
	for i in range(len(pip_packages)):
		pip_packages[i] = pip_packages[i].split()

	#Listing available packages in server

	# creating a socket to listen for incoming connections
	hello_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 4033
	hello_socket.connect(('192.168.43.15',port))
	hello_socket.send(("hello").encode('utf-8'))
	#time.sleep(2)
	package_list = []
	for i in range(2):
		m = hello_socket.recv(20).decode()
		package_list.append(m)
	hello_socket.close()

	return render_template("main.html",packages=packages,pip_packages=pip_packages,package_list=package_list)

if __name__ == '__main__':
	app.run(debug=True)


