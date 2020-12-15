'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''
with open('my_file.txt', 'w') as f:
    f.write('hello my dear\ntoday a good day\n')

num_lines = 0
num_words = 0

num_lines = sum(1 for line in open('my_file.txt'))
print(f'Число строк:', num_lines)

with open('my_file.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

    print(f'Количество букв:', num_words)
