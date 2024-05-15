class Vehicle:
    def __init__(self, make, model):
        self.make = make    # Марка транспортного средства
        self.model = model  # Модель транспортного средства
    
    def start(self):
        """Запуск транспортного средства"""
        print(f"{self.make} {self.model} заводится.")
    
    def stop(self):
        """Остановка транспортного средства"""
        print(f"{self.make} {self.model} останавливается.")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  
        self.num_doors = num_doors  
    
    def open_trunk(self):
        """Открытие багажника автомобиля"""
        print(f"Багажник {self.make} {self.model} открыт.")


class Bike(Vehicle):
    def __init__(self, make, model, type_bike):
        super().__init__(make, model)  
        self.type_bike = type_bike  
    
    def ring_bell(self):
        """Звонок на велосипеде"""
        print(f"{self.make} {self.model} звенит звонок!")

    def jump_in_mountaints(self):
        """С арматурами"""
        print(f"{self.make} {self.model} пригает по кочкам")


# Создание объектов класса Car
car1 = Car("Toyota", "Corolla", 4)

# Создание объектов класса Bike
bike1 = Bike("Giant", "Escape 3", "городской")

# Использование методов объектов класса Car
car1.start()
car1.open_trunk()
car1.stop()

# Использование методов объектов класса Bike
bike1.start()
bike1.ring_bell()
bike1.stop()
bike1.jump_in_mountaints()
