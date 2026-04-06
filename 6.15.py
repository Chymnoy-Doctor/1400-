a = float(input("Введите a: "))
s = 0
n = 1
while s <= a:
    s += 1 / n
    if s > a:
        print(f"n = {n}: сумма = {s:.6f}")
    n += 1