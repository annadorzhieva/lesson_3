"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def division_func():

        number_1 = int(input('Введите число 1: '))
        number_2 = int(input('Введите число 2: '))

        if number_1 == 0 or number_2 == 0:
                print('Деление на 0')

        result = number_1 / number_2

        return result

result = division_func()
print(f'Результат деления:', result)
