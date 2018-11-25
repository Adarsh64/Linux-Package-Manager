import socket

hello_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4018
hello_socket.connect(('192.168.43.15',port))
hello_socket.send(("hello").encode('utf-8'))
#time.sleep(2)
package_list = []
for i in range(2):
	m = hello_socket.recv(200).decode('utf-8').split(" ")
	package_list.append(m)
hello_socket.close()
print(package_list)
