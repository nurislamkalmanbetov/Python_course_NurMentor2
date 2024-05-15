# Определение класса Car
class Car:
    def __init__(self, make, model, year, color):
        self.make = make      # Марка автомобиля
        self.model = model    # Модель автомобиля
        self.year = year      # Год выпуска
        self.color = color    # Цвет автомобиля
        self.speed = 0        # Текущая скорость, изначально равна 0
    
    def accelerate(self, amount):
        """Увеличить скорость автомобиля на заданное значение"""
        self.speed += amount
        print(f"Автомобиль ускорился на {amount}км/ч. Текущая скорость:{self.speed} км/ч")
    
    def brake(self, amount):
        """Уменьшить скорость автомобиля на заданное значение"""
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Автомобиль замедлился на {amount} км/ч. Текущая скорость: {self.speed} км/ч.")    

    def honk(self):
        """Подать звуковой сигнал"""
        print("Биип Биип!")

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla", 2020, "Красный")

# Использование методов объекта
my_car.accelerate(30)  
my_car.brake(10)       
my_car.honk()          

# Доступ к атрибутам объекта
print(f"Моя машина {my_car.year} {my_car.make} {my_car.model}  {my_car.color} цвет.")

# __________________________________________________________________________________________

# Определение класса Student
class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Имя студента
        self.age = age    # Возраст студента
        self.grade = grade  # Оценка студента (например, средний балл)
    
    def study(self, hours):
        """Студент учится указанное количество часов"""
        print(f"{self.name} учится {hours} часов.")
    
    def take_exam(self, ocenka):
        """Студент сдает экзамен и получает балл"""
        self.grade = ocenka
        print(f"{self.name} сдал экзамен и получил {self.grade}.")

    def introduce(self, hobby):
        """Студент представляет себя"""
        print(f"Привет, я {self.name}. Мне {self.age} лет, и моя текущая оценка — {self.grade}. I love {hobby}")

# Создание объектов класса Student
student1 = Student("Алишер", 20, 85)
student2 = Student("Станислав", 22, 90)

# Использование методов объектов
student1.introduce("чтение")
student1.study(2)
student1.take_exam(55)

student2.introduce()
student2.study(2)
student2.take_exam()
student2.introduce()