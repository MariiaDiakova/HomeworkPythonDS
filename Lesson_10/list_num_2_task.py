''' 2 task Напишіть програму, яка б приймала список з числами
    та перевіряла чи всі числа в ньому унікальні. Реалізуйте
    у функції декілька обробок виключень.'''

import sys


class EmptyInputError(Exception):
    def __init__(self):
        super().__init__('Ви нічого не ввели! Пустий рядок!')


check_list = list(input('Введіть список чисел: '))


def list_num(check_list: list):
    try:
        if not all([c.isdigit() for c in check_list]):
            raise ValueError('Це не цифри!')
        if len(check_list) == 0:
            raise EmptyInputError()

        set_check = set(check_list)
        return len(check_list) == len(set_check)

    except ValueError:
        print('\nПомилка! Необхідно ввести числа!', file=sys.stderr)
        check_list = list(input('Введіть коректне значення (тільки числа!): '))
        set_check = set(check_list)
        return len(check_list) == len(set_check)

    except EmptyInputError:
        print('\nВи нічого не ввели! Пустий рядок', file=sys.stderr)
        check_list = list(input('Введіть коректне значення (тільки числа!): '))
        set_check = set(check_list)
        return len(check_list) == len(set_check)


print('Yes !)' if list_num(check_list) else 'No :(')
