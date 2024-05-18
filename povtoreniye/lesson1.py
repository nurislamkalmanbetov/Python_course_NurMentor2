# def my_function(*args):
#     for arg in args:
#         print(arg)

# # Вызов функции с различным количеством аргументов
# my_function(1, 2, 3)
# # Вывод:
# # 1
# # 2
# # 3

# my_function('a', 'b', 'c', 'd')
# # Вывод:
# # a
# # b
# # c
# # d

# ______________________________________________________ 

# def my_function(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     # print(f"{key}: {value}")

# # Пример вызова
# my_function(name='John', age=25, city='New York')
# # Вывод: {'name': 'John', 'age': 25, 'city': 'New York'}

# # ______________________________________________________ 

# def greet(name, job):
#     return f"Привет, {name}! Ты работаешь как {job}."

# # Примеры использования функции
# print(greet("Алексей", "программист"))

# print(greet("Мария", "дизайнер"))

# ______________________________________________________ 

# def create_file(file_path, content):
#     try:
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(content)
#             return f"Файл '{file_path}' успешно создан и записан."
#     except PermissionError:
#         return f"Ошибка: Нет доступа для записи файла по пути '{file_path}'."
#     except Exception as e:
#         return f"Произошла ошибка при создании файла: {e}"

# result = create_file("example.txt", "Привет, мир!\nЭто пример содержимого файла.")
# print(result)


# ______________________________________________________ 


# def read_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         return f"Ошибка: Файл по пути '{file_path}' не найден."
#     except PermissionError:
#         return f"Ошибка: Нет доступа к файлу по пути '{file_path}'."
#     except Exception as e:
#         return f"Произошла ошибка при чтении файла: {e}"
    
# file_content = read_file("example.txt")
# print(file_content)

# ______________________________________________________________________________________________ 


# class Employee:
#     def __init__(self, name, position, salary, bonus):
#         self.name = name  # Публичный атрибут
#         self.position = position  # Публичный атрибут
#         self.__salary = salary  # Приватный атрибут
#         self._bonus = bonus  # Тайный атрибут

#     def get_salary(self):
#         return self.__salary  # Геттер для приватного атрибута

#     def set_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary  # Сеттер для приватного атрибута
#         else:
#             print("Заработная плата должна быть неотрицательной.")

#     def get_bonus(self):
#         return self._bonus  # Геттер для тайного атрибута

#     def set_bonus(self, new_bonus):
#         self._bonus = new_bonus  # Сеттер для тайного атрибута

# # Пример использования класса
# employee = Employee("Иван", "Программист", 5000, 1000)

# # Доступ к публичным атрибутам
# print("Имя работника:", employee.name)
# print("Должность работника:", employee.position)

# # Доступ к приватному атрибуту через геттер
# print("Заработная плата работника:", employee.get_salary())

# # Изменение приватного атрибута через сеттер
# employee.set_salary(20000)
# print("Новая заработная плата работника:", employee.get_salary())

# # Доступ к тайному атрибуту
# print("Бонус работника:", employee.get_bonus())

# # Изменение тайного атрибута
# employee.set_bonus(3500)
# print("Новый бонус работника:", employee.get_bonus())

# _____________________________________________________________________________________________ 

# полиморфизм 

# class Cat:
#     def make_sound(self):
#         return "Мяу"

# class Dog:
#     def make_sound(self):
#         return "Гав"

# def make_sound_of_animal(animal):
#     return animal.make_sound()

# # Пример использования
# cat = Cat()
# dog = Dog()

# print(make_sound_of_animal(cat))  # Вывод: Мяу
# print(make_sound_of_animal(dog))  # Вывод: Гав

# __________________________________________________ 

# def decorator(func):
#     def wrapper():
#         print("Действие до выполнения функции1")
#         func()
#         print("Действие после выполнения функции2")
#     return wrapper

# @decorator
# def hello():
#     print("Hello world!")

# hello()

