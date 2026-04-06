a = float(input("Введите a (1 < a <= 1.5): "))
k = 2
while True:
    value = 1 + 1 / k
    if value < a:
        break
    print(f"{value:.4f}")
    k += 1