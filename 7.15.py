m = int(input("Введите количество чисел: "))
n = int(input("Введите n: "))
total = 0
for i in range(1, m + 1):
    x = int(input(f"Введите x{i}: "))
    if x % n == 0:
        total += x
print(f"Сумма чисел, кратных {n}: {total}")