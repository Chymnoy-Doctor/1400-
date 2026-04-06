# Задача 7.3
a = int(input("Введите a: "))
b = int(input("Введите b (b >= a): "))

total = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        total += i

print(f"Сумма чисел от {a} до {b}, кратных 5: {total}")