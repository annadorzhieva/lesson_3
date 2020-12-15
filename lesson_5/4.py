'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

numbers = 'One — 1\nTwo — 2\nThree — 3\nFour — 4'
with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(numbers)

ru = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

new_numbers = []
with open('numbers.txt', 'r') as f:
    for el in f:
        el = el.split(' ', 1)
        new_numbers.append(ru[el[0]] + el[1])
    print(new_numbers)