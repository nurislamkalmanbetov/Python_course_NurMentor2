# # Определение декоратора
# def my_decorator(func):
#     def wrapper():
#         print("Декоратор выполняется")
#         func()
#     return wrapper

# # Использование декоратора
# @my_decorator
# def say_hello():
#     print("Привет!")

# # Вызов функции
# say_hello()

# _________________________________________________________________________


# Определение декоратора
# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит перед вызовом функции")
#         func()  # Вызов функции, переданной в качестве аргумента
#         print("Что-то происходит после вызова функции")
#     return wrapper

# # Использование декоратора
# @my_decorator
# def say_hello():
#     print("Привет, мир!")

# # Вызов функции, обернутой в декоратор
# say_hello()

# _________________________________________________________________________

# Определение декоратора
# def print_function_name(func):
#     def wrapper(*args, **kwargs):
#         print(f"Выполняется функция: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# # Использование декоратора
# @print_function_name
# def greet(name):
#     print(f"Привет, {name}!")

# # Вызов функции
# greet("Миша")
# _________________________________________________________________________

# Функция uppercase принимает функцию func в качестве аргумента и 
# возвращает новую функцию wrapper.
# Функция wrapper принимает аргумент text, приводит его к верхнему 
# регистру и передает его в функцию func. Затем возвращает результат 
# вызова func.
# Декоратор @uppercase указывает, что функция greet должна быть 
# обернута декоратором uppercase.
# Когда вызывается greet("Alice"), на самом деле выполняется wrapper, 
# который вызывает greet с аргументом в верхнем регистре 
# ("ALICE"). Функция greet добавляет приветствие к этому имени и 
# возвращает результат.

# def uppercase(func):
#     def wrapper(text):
#         result = func(text.upper())
#         return result
#     return wrapper

# @uppercase
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))




