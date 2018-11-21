from flask import *
import subprocess
import socket
import time
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
	return render_template("main.html",packages=packages,pip_packages=pip_packages)

if __name__ == '__main__':
	app.run(debug=True)


