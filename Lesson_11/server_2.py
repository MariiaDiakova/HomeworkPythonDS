''' 2 task Додайте до серверу з першого завдання функцію чат-боту,
    який би відсилав клієнту задані відповіді на певні повідомлення.'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("", 55000))
sock.listen(10)
print('Server is running')

while True:
    conn, addr = sock.accept()
    print('Connected: ', addr)
    data = conn.recv(1024).decode('UTF-8')

    print(data)
    if data == 'Hello':
        answer = 'Hi!'
    elif data == 'How are you?':
        answer = 'OK :)'
    elif data == 'Good bye!':
        answer = 'Bye bye!'
    else:
        answer = 'I do not understand you('

    conn.send(bytes(answer, encoding='UTF-8'))

conn.close()
