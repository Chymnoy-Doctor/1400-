a = float(input("Введите a (1 < a <= 1.5): "))
n = 2
while True:
    value = 1 + 1 / n
    if value < a:
        break
    print(f"n = {n}: {value:.4f}")
    n += 1