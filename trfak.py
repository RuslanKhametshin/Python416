import os

file_path = "\\Python\\proverka.txt"

if os.path.exists(file_path):
    directory, name = os.path.split(file_path)
    atime = os.path.getatime(file_path)
    print(f"{name} ({directory}) - время последнего доступа к файлу {atime} секунд")
else:
    print(f"Файл {file_path} не существует")