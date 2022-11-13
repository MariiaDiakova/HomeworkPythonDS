''' 1 task Напишіть функцію, яка б приймала номер місяця,
    а вертала його назву. Реалізуйте у функці
    декілька обробок виключень.'''

month_num = input('Введіть номер місяця: ')


def month(month_num: str) -> str:
    dict_month = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень',
                  7: 'Липень', 8: 'Серпень', 9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}

    try:
        month_num = int(month_num)
        result = dict_month[month_num]
        return result

    except KeyError:
        print('Помилка! Такого місяця не існує!')
        month_num = int(input('Введіть коректне значення: '))
        result = dict_month.get(month_num)
        return result

    except ValueError:
        print('Помилка! Необхідно ввести НОМЕР місяця!')
        month_num = int(input('Введіть коректне значення: '))
        result = dict_month.get(month_num)
        return result


print(month(month_num))
