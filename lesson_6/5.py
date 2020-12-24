'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery(object):
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Пишем ручкой'

class Pencil(Stationery):
    def draw(self):
        return f'Рисуем карандашом'

class Handle(Stationery):
    def draw(self):
        return f'Подчёркиваем маркером'

p = Pen('pen')
print(p.draw())
pn = Pencil('pencil')
print(pn.draw())
h = Handle('handle')
print(h.draw())

