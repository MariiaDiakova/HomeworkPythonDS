''' 3 task Напишіть користувацький клас виключення
    з функціоналом на свій вибір.
    Викличте його за допомогою інструкції raise.'''


# Викликається у task 2 (raise EmptyInputError())

class EmptyInputError(Exception):
    def __init__(self, *args):

        if len(args) == 0:
            msg = 'Ви нічого не ввели! Пустий рядок!'
        else:
            msg = args[0]

        super().__init__(msg)

    def __str__(self):

        msg = super().__str__()
        return f'{self.__class__.__name__}: {msg}'
