results = []
for num in range(10, 100):
    s = num // 10 + num % 10
    if s + s ** 2 == num:
        results.append(num)
print(f"Двузначные числа, удовлетворяющие свойству: {results}")