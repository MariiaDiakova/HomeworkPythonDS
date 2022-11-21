''' 1 task Реалізувати чат без графічного інтерфейсу,
    який дозволить обміняватися повідомленнями між клієнтом та
    сервером. Клієнт повинен отримувати повідомлення сервера.'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("", 55000))
sock.listen(10)
print('Server is running')

while True:
    conn, addr = sock.accept()
    print('Connected: ', addr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data * 2)

conn.close()
