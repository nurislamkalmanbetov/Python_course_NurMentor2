# ООП - Объектно Ориентированное Программирование 

# 1) Наследование 
# 2) Полиморфизм 
# 3) Абстракиця 
# 4) Инкапсуляция 

# class Имя_класса:
#     методы 


# ___________________________________________________________________

# Class 

                    # атрибуты
# class Person():     #   \/  
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
        
#         #  метод
#         #   \/
#     def say_hello(self):
#         print(f'Hello {self.name}! You are {self.age} years old!')

 
#         #  Пример Экземпляр
#         #    \/
# exemplyar_class = Person("Nurislam", 27)  
# exemplyar_class.say_hello()

# name = 'John'
# name.lower()


# ___________________________________________________________________

# Наследование 

# class Human:
#     def walk(self):
#         print(f'walking')


# class Student(Human):
#     def study(self):
#         print(f'studying')

    
# # Man = Human()
# # Man.walk()

# Teenaidjer = Student()
# Teenaidjer.study()
# Teenaidjer.walk()


# ___________________________________________________________________

# Множественное наследование 

# class A:
#     def click(self):
#         print("Это А")

# class B(A):
#     def click(self):
#         print("Это В")

# class C(B): 
#     def click(self):
#         print("Это С")

# class D(B,C):
#     pass 


# name = D()
# name.click()


# ___________________________________________________________________

# Полиморфизм 


# class Animals:
#     def __init__(self, name):
#         self.name = name 

#     def say(self):
#         print(f'{self.name} Издает звук')


# class Dog(Animals):
#     def say(self):
#         print(f'{self.name} лает')

# class Cat(Animals):
#     def say(self):
#         print(f'{self.name} мюкает')

# class Human:
#     def __init__(self, name):
#         self.name = name 

#     def say(self):
#         print(f'{self.name} говорит')


# Rex = Dog('Rex')
# Rex.say()
# Tom = Cat('Tom')
# Tom.say()
# Nuris = Human('Nuris')
# Nuris.say()

# ___________________________________________________________________

# Инкапсуляция 
# 1) Публичная 
# 2) Защищенная 
# 3) Приватная

# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self):
#         print("Hello")


# bank = Bank('Bob', 1000)
# bank.__set_balance()

# ___________________________________________________________________

# Абстракция 







