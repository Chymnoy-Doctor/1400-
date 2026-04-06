c = []
for i in range(1, 16):
    val = float(input(f"Введите c{i}: "))
    c.append(val)
total = 0
for i in range(0, 15, 2):  # индексы 0,2,4,... соответствуют c1,c3,c5,...
    total -= c[i]
print(f"Результат: {total:.2f}")