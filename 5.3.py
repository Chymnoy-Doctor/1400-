price_per_kg = float(input("Введите цену 1 кг конфет: "))
print("Вес (кг)\tСтоимость")
for kg in range(1, 11):
    cost = price_per_kg * kg
    print(f"{kg}\t\t{cost:.2f}")