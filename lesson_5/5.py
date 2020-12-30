'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
my_num = input('Введите набор чисел: ')
with open('file_num.txt', 'w') as f:
    f.write(my_num)
    print(my_num)

with open('file_num.txt', 'r') as f:
    a = f.read().split()
    s = 0
    for el in a:
        s += int(el)
    with open('file_num_new.txt', 'w') as g:
        g.write(str(s)+ '\n')