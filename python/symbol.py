kolvo = int(input("Введите количество символов: "))
symbol = input("Введите тип символа: ")
orientation = int(input("Введите ориентацию линии (0 - горизонтальная, 1 - вертикальная): "))
if orientation == 0:
    a = 0
    while a < kolvo:
        print(symbol, end="")
        a += 1
elif orientation == 1:
    a = 0
    while a < kolvo:
        print(symbol)
        a += 1
else:
    print("Введите корректное значение: ")
