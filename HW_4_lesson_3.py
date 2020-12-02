"""Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

def my_func(x, y):
    return x**y

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

result = my_func(x, y)
print(f'Ваш результат возведения в отрицательныю степень: ', result)

def my_func_1(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

result_1 = my_func_1(x, y)
print(f'Ваш второй результат возведения в отрицательную степень: ', result_1)

