"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов"""

def my_func(num_1, num_2, num_3):
    # max(arg_1, arg_2, arg_3)
    a = num_1+num_2
    b = num_1+num_3
    c = num_2+num_3
    # max_number = max(int(a, b, c))
    # return max_number
    print(max(a, b, c))

my_func(2, 12, 19)

