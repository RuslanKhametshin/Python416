class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_rect(self):
        print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")


class RectFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print("Фон:", self.fon)

class RectBorder(Rect):
    def __init__(self, width, height, border_width, border_type, border_color):
        super().__init__(width, height)
        self.border_width = border_width
        self.border_type = border_type
        self.border_color = border_color

    def show_rect(self):
        super().show_rect()
        print(f"Ширина рамки: {self.border_width}")
        print(f"Тип рамки: {self.border_type}")
        print(f"Цвет рамки: {self.border_color}")


shape1 = RectFon(400, 200, "yellow")
shape1.show_rect()
print()
shape2 = RectBorder(600, 300, "1px", "solid", "red")
shape2.show_rect()