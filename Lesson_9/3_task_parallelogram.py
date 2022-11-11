''' 3 task Напишить клас Parallelogram, який приймає два
    аргументи width і length і метод get_area,
    який вираховує площу паралелограму. Успадкуйте від
    нього клас Square, перевизначіть в ньому метод
    get_area таким чином, щоб він вираховував площу квадрату.'''


class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        s_parallelogram = self.length * self.width
        return s_parallelogram


sp = Parallelogram(5, 6)
print(f'Площа паралелограма: {sp.get_area()}')


class Square(Parallelogram):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(5)
print(f'Площа квадрату: {square.get_area()}')
