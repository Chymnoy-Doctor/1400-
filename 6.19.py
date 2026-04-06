total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(f"Сумма чисел от 100 до 500, кратных 3: {total}")