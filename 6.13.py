a = float(input("Введите a: "))
s = 0
k = 1
while True:
    s += 1 / k
    if s >= a:
        break
    print(f"{s:.6f}")
    k += 1