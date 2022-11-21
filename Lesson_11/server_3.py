''' 3 task Напишіть сервер, який би отримував у користувача фразу,
    а потім надсилав би підраховану кількість слів у відповідь.'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("", 55000))
sock.listen(10)
print('Server is running')

while True:
    conn, addr = sock.accept()
    print('Connected: ', addr)
    data = conn.recv(1024).decode('UTF-8')
    print(str(data))
    data = len(data.split(' '))
    conn.send(bytes(str(data), encoding='UTF-8'))

conn.close()
