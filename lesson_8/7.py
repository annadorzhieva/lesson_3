'''
 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
 и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
 и умножение созданных экземпляров. Проверьте корректность полученного результата
'''
class Operation():
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * j'

    def __add__(self, other):
        print('Сумма двух комплексных чисел')
        return print(f'c = {self.a + other.a} + {self.b + other.b} * j')

    def __mul__(self, other):
        print('Умножение комплексных чисел')
        return print(f'c = {self.a - other.a} + {self.b + other.b} * j')

op_1 = Operation(1,2)
op_2 = Operation(2,3)
print(op_1+op_2)
print(op_1 * op_2)