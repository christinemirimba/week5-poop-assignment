class Car:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year
        self._is_running = False
        self.__mileage = 0 

    # Method to start the car
    def start(self):
        self._is_running = True
        return f"{self.brand} {self.model} ({self.year}) is running!"
    
    # Method to stop the car
    def stop(self):
        self._is_running = False
        return f"{self.brand} {self.model} stopped!"
    
    # Method to add mileage
    def add_mileage(self, km):
        self.__mileage += km

    # Method to get mileage
    def get_mileage(self):
        return f"Mileage: {self.__mileage} km"


# Sub class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery):
        super().__init__(brand, model, year)  
        self.battery = battery

    # Polymorphism (override start())
    def start(self):
        return f"{self.brand} {self.model} ({self.year}) starts (electric)."


# Creating objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = ElectricCar("Tesla", "Model 3", 2023, 75)

print(car1.start())
car1.add_mileage(100)
print(car1.get_mileage())

print(car2.start())  
car2.add_mileage(200)
print(car2.get_mileage())
