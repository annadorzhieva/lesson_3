'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''
class Car(object):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала, '
    def stop(self):
        return f'остановилась.'
    def turn(self):
        return f'повернула, '
    def show_speed(self):
        return f'Скорость машины', self.speed

class TownCar(Car):
    def info_TownCar(self):
        return f'Машина для города'
    def show_speed(self):
        if self.speed > 60:
           return f'Превышение скорости'
        else:
            return f'Скорость оптимальная'

class SportCar(Car):
    def info_SportCar(self):
        return f'Спортивная машина'

class WorkCar(Car):
    def info_WorkCar(self):
        f'Грузовая машина'
    def show_speed(self):
        if self.speed > 40:
           return f'Превышение скорости'
        else:
            return f'Скорость оптимальная'

class PoliceCar(Car):
    def info_PoliceCar(self):
        return f'Полицеская машина'

tc = TownCar(70, 'red', 'Mazda', True)
print(tc.go(), tc.turn(), tc.show_speed())
wc = WorkCar(40, 'black', 'Iveco', False)
print(wc.go(), wc.show_speed())

