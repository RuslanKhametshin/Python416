sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}
for name, regions in sales.items():
    print(name)
    for region, value in regions.items():
        print(region, ":", value)
name = input("Имя: ")
region = input("Регион: ")
if name in sales and region in sales[name]:
    print(sales[name][region])
    new_value = int(input("Новое значение: "))
    sales[name][region] = new_value
    print(sales[name])
else:
    print("Такого имени или региона нет в базе данных.")
