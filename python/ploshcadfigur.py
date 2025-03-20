import  math

print("Вычисление площади фигур")
print("Выбери фигуру: ")
print("1 - треугольник")
print("2 - прямоугольник")
print("3 - круг")

vibor = int(input(": "))
if vibor == 1:
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b =  "))
    c = float(input("Введите сторону c =  "))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(round(area, 2))
elif vibor == 2:
    a = float(input("Введите длину a = "))
    b = float(input("Введите ширину b = "))
    area = a * b
    print(round(area, 2))
elif vibor == 3:
    r = float(input("Введите радиус r = "))
    area = math.pi * r**2
    print(round(area, 2))
else:
    print("Выберете фигуру!")