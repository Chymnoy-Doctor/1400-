n = int(input("Введите натуральное число: "))
total = 0
for d in range(1, n + 1):
    if n % d == 0 and d % 2 == 0:
        total += d
print(f"Сумма чётных делителей числа {n}: {total}")