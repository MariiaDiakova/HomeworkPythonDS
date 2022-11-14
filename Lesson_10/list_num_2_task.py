''' 2 task Напишіть програму, яка б приймала список з числами
    та перевіряла чи всі числа в ньому унікальні. Реалізуйте
    у функції декілька обробок виключень.'''

from my_custom_error_3_task import EmptyInputError
import sys

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

    except EmptyInputError as ex:
        print(f'\n{ex}', file=sys.stderr)
        check_list = list(input('Введіть коректне значення (тільки числа!): '))
        set_check = set(check_list)
        return len(check_list) == len(set_check)


print('Yes !)' if list_num(check_list) else 'No :(')
