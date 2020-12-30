'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
'''
class Office_equipment():
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.my_store = []
        self.my_dict = {'Название': self.name, 'Количество': self.number}

    def moving(self):
        try:
            unit = input(f'Введите наименование ')
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Количество': unit_q}
            self.my_dict.update(unique)
            self.my_store.append(self.my_dict)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

unit_1 = Office_equipment('hp', 10)
unit_2 = Office_equipment('Canon', 5)
print(unit_1.moving())
print(unit_2.moving())
