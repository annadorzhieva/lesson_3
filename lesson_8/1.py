'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Data():
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
        print('Дата: ', self.d, '-', self.m, '-', self.y)

    @classmethod
    def my_method(cls, d, m, y):
        pass

    @staticmethod
    def number(d, m, y):
        if d >=1 or d <= 31:
            if m >=1 or m <= 12:
                if y >= 2020 or y < 0:
                    return print('Всё верно')
                else:
                    return print('Измените год')
            else:
                return print('Измените месяц')
        else:
            return print('Измените день')


data = Data(26, 12, 2020)
print(Data.number(20, 11, 2020))