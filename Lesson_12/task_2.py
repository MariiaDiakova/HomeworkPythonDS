''' 2 Task Розробіть сокет сервер з використанням бібліотеки asyncio.
    Сервер повине приймати два числа і проводити над ними прості
    арифметичні функції - додавання, віднімання, множення, ділення -
    з використанням користувацьких функцій, які працюють в асинхронному режимі.'''

import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("", 55000))
sock.listen(10)
print('Server is running')

while True:
    conn, addr = sock.accept()
    print('Connected: ', addr)
    data = conn.recv(1024).decode('UTF-8')
    entered_list = data.split()
    num_list = list(map(int, entered_list))

    async def addition(num_list):
        res = sum(num_list)
        print(f'Addition: {res}')
        await asyncio.sleep(1)
        return res

    async def subtraction(num_list):
        res = num_list[0] - num_list[1]
        print(f'Subtraction: {res}')
        await asyncio.sleep(2)
        return res

    async def multiplication(num_list):
        res = num_list[0] * num_list[1]
        print(f'Multiplication: {res}')
        await asyncio.sleep(2)
        return res

    async def division(num_list):
        res = num_list[0] / num_list[1]
        print(f'Division: {res}')
        await asyncio.sleep(3)
        return res


    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(addition(num_list), name="Add"),
        ioloop.create_task(subtraction(num_list), name="Subtract"),
        ioloop.create_task(multiplication(num_list), name="Multiply"),
        ioloop.create_task(division(num_list), name="Divide")
    ]
    results, _ = ioloop.run_until_complete(asyncio.wait(tasks))

    response = "\n".join([f"{t.get_name()}: {t.result()}" for t in results])
    conn.send(bytes(str(response), encoding='UTF-8'))

ioloop.close()
conn.close()
