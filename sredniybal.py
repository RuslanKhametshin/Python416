kol_students = int(input("Количество студентов: "))
students = {}
for i in range(1, kol_students + 1):
    print(str(i) + "-й студент:", end=" ")
    name = input()
    print("Балл: ", end=" ")
    bal = int(input())
    students[name] = bal
sredbal = sum(students.values()) / kol_students
print("Средний балл: ", round(sredbal), ". Студенты с баллом выше среднего: ")
for name, bal in students.items():
    if bal > sredbal:
        print(name)