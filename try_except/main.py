# №1

# try:
#     # Попытка выполнить код, который может вызвать ошибку
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     # Обработка ошибки
#     print("Ошибка! Введено некорректное значение.")

# ______________________________________________________________ 

# №2

# try:
#     file = open("example.txt", "r") # -r - читать 
#     content = file.read()
#     print("Содержимое файла:")
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("Ошибка: файл не найден")
# except IOError:
#     print("Ошибка: не удалось прочитать файл")

# ______________________________________________________________ 

# №3 

# try:
#     dividend = int(input("Введите делимое: "))
#     divisor = int(input("Введите делитель: "))
    
#     result = dividend / divisor
    
#     print("Результат деления:", result)
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль")

# ______________________________________________________________ 

# №4

# def get_username(user_dict, user_id):
#     try:
#         username = user_dict[user_id]
#         return username
#     except KeyError:
#         print("Ошибка: пользователь с таким ID не найден")
#         return None

# # Пример вызова функции get_username():
# users = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie"
# }

# print(get_username(users, 2))   # Вывод: Bob
# print(get_username(users, 5))   # Вывод: Ошибка: пользователь с таким ID не найден; None

# ____________________________

# def get_username(user_dict):
#     try:
#         user_id = int(input("Введите ID пользователя: "))
#         username = user_dict[user_id]
#         return username
#     except KeyError:
#         print("Ошибка: пользователь с таким ID не найден")
#         return None
#     except ValueError:
#         print("Ошибка: введите целое число в качестве ID")
#         return None

# # Пример вызова функции get_username():
# users = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie"
# }

# username = get_username(users)
# if username is not None:
#     print("Имя пользователя:", username)

# ____________________________

# def get_username(user_dict):
#     while True:
#         user_input = input("Введите ID пользователя (для выхода введите 'exit'): ")
#         if user_input == 'exit':
#             print("Программа завершена.")
#             return
#         try:
#             user_id = int(user_input)
#             username = user_dict[user_id]
#             print("Имя пользователя:", username)
#         except KeyError:
#             print("Ошибка: пользователь с таким ID не найден")
#         except ValueError:
#             print("Ошибка: введите целое число в качестве ID")

# # Пример вызова функции get_username():
# users = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie"
# }

# get_username(users)

# ____________________________
