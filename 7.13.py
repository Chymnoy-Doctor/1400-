n = int(input("Введите количество чисел: "))
p = float(input("Введите p: "))
total = 0
for i in range(1, n + 1):
    b = float(input(f"Введите b{i}: "))
    if b > p:
        total += b
print(f"Сумма чисел, больших {p}: {total:.2f}")