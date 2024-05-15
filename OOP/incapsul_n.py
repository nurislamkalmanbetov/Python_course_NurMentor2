class Person:
    def __init__(self, name, age, money):
        self.__name = name    # Имя (закрытый атрибут)
        self.__age = age      # Возраст (закрытый атрибут)
        self.__money = money  # Деньги (закрытый атрибут)

    def earn_money(self, amount):
        """Зарабатывает деньги"""
        self.__money += amount

    def spend_money(self, amount):
        """Тратит деньги"""
        if self.__money >= amount:
            self.__money -= amount
            print(f"{self.__name} потратил {amount} KGS.")
        else:
            print(f"Недостаточно денег для траты.")

    def get_name(self):
        """Возвращает имя"""
        return self.__name

    def get_age(self):
        """Возвращает возраст"""
        return self.__age

    def get_money(self):
        """Возвращает количество денег"""
        return self.__money

# Создание объекта класса Person для Нурислама
nurislam = Person("Нурислам", 25, 10000)

# Изменение количества денег с помощью метода earn_money
nurislam.earn_money(5000)

# Попытка траты денег
nurislam.spend_money(7000)

# Получение информации о Нурисламе через методы
print("Имя:", nurislam.get_name())
print("Возраст:", nurislam.get_age())
print("Количество денег:", nurislam.get_money())
