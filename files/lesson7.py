# Работа с файлами

# r: Открывает файл для чтения.
# w: Открывает файл для записи (и стирает содержимое, если файл уже существует).
# a: Открывает файл для добавления (записи в конец файла).
# +: Разрешает чтение и запись в файле.

# __________________________________________________________________________________

# file = open('test1.txt', 'w') # w - пишет в файл 
# file.write('Hello world')
# file.close()
# print()

# __________________________________________________________________________________

# file = open('test.txt', 'r') # r - читает файл 
# context = file.read()
# print(context)
# file.close()

# __________________________________________________________________________________

# file = open('test.txt', 'a') # a - добавляет поверх текст 
# file.write('\nHello world')
# file.close()

# __________________________________________________________________________________

# with open('test.txt', 'r') as file:
#     context = file.read()
#     print(context)

# __________________________________________________________________________________

# with open('test.txt', 'w', encoding='utf-8') as file: # пишет в файл 
#     file.write('Здравствуйфффффффффф')


# ________________________________________________________________________

# add names into files 

# names = ['John', 'Alice', 'Michael', 'Emily', 'David']

# with open('test.txt', 'a+') as n:
#     for name in names:
#         n.write(name + '\n')

# ________________________________________________________________________

# names = ['John', 'Alice', 'Michael', 'Emily', 'David']

# with open('test.txt', 'a+') as n:
#     for name in names:
#         n.write(name + '\n')
#     n.seek(7)    # начинает с индекса в списке
#     a = n.read()
#     print(a)

# __________________________________________________________________________________

# with open('test1.txt', 'r') as file:
#     content = file.read()
#     if 'Python' in content:
#         print('Yes')
#     else:
#         print('No')
