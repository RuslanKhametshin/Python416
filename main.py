# name = "admin"  # переменная
#
# # print("Hello,", name)
# age = 20
# # print(name + str(age))
# print(age)
# age = 15.2
# print(age)
# print(type(name))  #str- обычная строка
# print(type(age))   #int- целочисловое значение, float-вещестенное число ~15.3
from collections.abc import async_generator

# a = 4
# b = 5
# print(id(a))  # показывает адрес нахождения в памяти в ячейке, нужно для проверки изменемых и не изменяемых типов данных
# print(id(b))
# a = b
# print(a)
# print(id(a))
# print(id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "hello", 9.2  # объявление переменных в одну строку
# print(a)
# print(b)
# print(c)

# _first_name = "admin"
# print(_first_name)


# import keyword
# keyword.kwlist ключевые слова

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет." )

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
#
# print("a:", a)
# print("b:", b)


# Принцип Исключения!!!!!!!!!!

# import os
#
# import os.path

# print(os.path.split(r"C:\Users\GanlucaGotti\Desktop\JS\H_10\task\text5.txt"))
#
# print(os.path.join(r"C:\Users", "GanlucaGotti", "Desktop", "JS", "H_10" "task", "text5.txt"))

import os

dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)

files = {
    "Work": ["w.txt"],
    r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
    r"Work\F2\F21": ["f211.txt", "f212.txt"]
}

for d, files in files.items():
    for file in files:
        file_path = os.path.join(d, file)
        open(file_path, "w").close()

file_width_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]

for file in file_width_text:
    with open(file, "w", encoding="utf-8") as f:
        f.write(f"Какой-то текст в файле {file}")

def print_tree(root, topdown):
    print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
    for root, directory, file_name in os.walk(root, topdown):
        print(root)
        print(directory)
        print(file_name)
    print("-" * 50)
print_tree("Work", False)
print_tree("Work", True)