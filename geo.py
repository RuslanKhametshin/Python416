import math
class Geometry:
    count = 0
    @staticmethod
    def triangle_heron(a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        Geometry.count += 1
        return area
    @staticmethod
    def triangle_base(base, height):
        area = 0.5 * base * height
        Geometry.count += 1
        return area
    @staticmethod
    def square(side):
        area = side * side
        Geometry.count += 1
        return area
    @staticmethod
    def rectangle(length, width):
        area = length * width
        Geometry.count += 1
        return area
    @staticmethod
    def get_count():
        return Geometry.count
print("Площадь треугольника по формуле Герона (3, 4, 5): ", Geometry.triangle_heron(3, 4, 5))
print("Площадь треугольника через основание и высоту (6, 7): ", Geometry.triangle_base(6, 7))
print("Площадь квадрата (7): ", Geometry.square(7))
print("Площадь прямоугольника(2, 6): ", Geometry.rectangle(2, 6))
print("Количество подсчетов площади: ", Geometry.get_count())