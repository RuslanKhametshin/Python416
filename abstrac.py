from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        for _ in range(self.side):
            print('*' * self.side)

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()

class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        for _ in range(self.width):
            print('*' * self.length)

    def info(self):
        print("===Квадрат===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()

class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Геронова формула
        s = self.perimeter() / 2
        return round((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5, 2)

    def perimeter(self):
        return self.a + self.b + self.c

    def draw(self):
        for i in range(1, 6):
            print(' ' * (6 - i) + '*' * (2 * i - 1))

    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.a}")
        print(f"Сторона 2: {self.b}")
        print(f"Сторона 3: {self.c}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()

# Пример использования:
shapes = [
    Square(3, "red"),
    Rectangle(3, 7, "green"),
    Triangle(11, 6, 2.5, "yellow")
]

for shape in shapes:
    shape.info()