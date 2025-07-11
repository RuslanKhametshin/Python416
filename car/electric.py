from .car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery_power=100):
        super().__init__(brand, model, year, mileage)
        self.battery_power = battery_power

    def display_info(self):
        super().display_info()
        print(f"Этот автомобиль имеет мощность {self.battery_power}%")