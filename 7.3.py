total = 0
for i in range(10, 51):
    if i % 10 == 5:
        total += i ** 2
print(f"Сумма квадратов чисел от 10 до 50, оканчивающихся на 5: {total}")