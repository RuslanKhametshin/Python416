class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufactur = ""
        self.engine_power = ""
        self.color = ""
        self.price = 0
    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufactur = input("Введите производителя: ")
        self.engine_power = input("Введите мощность двигателя: ")
        self.color = input("Введите цвет машины: ")
        self.price = int(input("Введите цену: "))
    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\n Год выпуска: {self.year}\n "
              f"Производитель: {self.manufactur}\n Мощность двигателя: {self.engine_power}\n "
              f"Цвет: {self.color}\n Цена: {self.price}")
        print("=" * 40)
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price
    def get_year(self):
        return self.year
car1 = Car()
car1.input_data()
car1.print_info()

print("Год выпуска:", car1.get_year())