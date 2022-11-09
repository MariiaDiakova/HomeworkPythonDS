def main_function():

    def seasons_year(a):

        if a > 12 or a < 1:
            return 'Такого місяця немає!'

        if a == 12 or a == 1 or a == 2:
            return 'Зима'
        elif a == 3 or a == 4 or a == 5:
            return 'Весна'
        elif a == 6 or a == 7 or a == 8:
            return 'Літо'
        else:
            return 'Осінь'

    def new_dict(*args):
        add_dict = {}

        for arg in args:
            add_dict.update(arg)

        return add_dict

    def pallindrom_chek(a):

        return a == a[::-1]

    def sum_num(number_of_count: int) -> int:
        str_format = str(number_of_count)
        list_format = list(str_format)

        for index in range(len(list_format)):
            list_format[index] = int(list_format[index])

        return sum(list_format)
