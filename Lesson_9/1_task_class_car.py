''' 1 task Напишіть клас автомобіля з атрибутами:
    -марка, колір, обєм двигуна.
    Та методами:
    -їхати вперед, їхати назад.
    Напишіть ще один клас автомобіля, який є успадкованим
    від першого. Додайте в нього методи повороту праворуч
    та ліворуч.'''


class Car(object):
    def __init__(self, brand, color, volume_engine):
        self.brand = brand
        self.color = color
        self.volume_engine = volume_engine

    def drive_forward(self):
        return "Їхати вперед"

    def drive_backward(self):
        return "Їхати назад"


class Car2(Car):
    def turn_right(self):
        return 'Поворот праворуч'

    def turn_left(self):
        return 'Поворот ліворуч'


mercedes = Car('Mercedes', 'red', 3)
audi = Car2('Audi', 'black', 2)

print(f'Moжливість першого класу Car: {mercedes.drive_forward()}, {mercedes.drive_backward()}')
print(f'Moжливість другого класу Car2: {audi.drive_forward()}, {audi.drive_backward()}, {audi.turn_right()}, {audi.turn_left()}')

