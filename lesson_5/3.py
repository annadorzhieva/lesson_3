'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''

wokers = 'Smith 11200\n'
wokers += 'Jones 15700\n'
wokers += 'Bin 21200\n'

with open('wokers.txt', 'w') as f:
    f.write(wokers)

with open('wokers.txt', 'r') as f:
    wokers = {}
    for line in f:
        key, value = line.split()
        wokers[key] = value
        if int(value) < 20000:
            print(f'{key}: оклад менее 20тыс.')