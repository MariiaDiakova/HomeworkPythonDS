import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

message = input('Enter message: ')
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024).decode('UTF-8')
print(data)

sock.close()
