'''
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''
class Storage():
    def __init__(self):
        print('Склад оргтехники')


class Office_equipment(Storage):
    def param(self, paper_size, type_ink):
        self.paper_size = paper_size
        self.type_ink = type_ink #тип чернил
        print('Виды оргтехники')

class Printer(Office_equipment):
    def param_printer(self, lazer):
        self.lazer = lazer
        return print('Лазерный принтер')

class Scanner(Office_equipment):
    def param_scanner(self, jet):
        self.jet = jet
        print('Струйный сканер')

class Copier(Office_equipment):
    def param_copier(self, copier):
        self.copier = copier
        print('Ксерокс')

office = Office_equipment()
pr = Printer()
print(pr.param_printer(lazer=1))
sc = Scanner()
print(sc.param_scanner(jet=2))