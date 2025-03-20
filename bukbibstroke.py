a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
c = set(a) - set(b)
print("Искомыми буквами являются: ", end=" ")
for iskomie in c:
    print(iskomie, end=" ")
