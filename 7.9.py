results = []
for num in range(100, 1000):
    if num % 7 == 0:
        s = sum(int(d) for d in str(num))
        if s % 7 == 0:
            results.append(num)
print(f"Трёхзначные числа, кратные 7 и с суммой цифр, кратной 7: {results[:10]}...")
print(f"Всего: {len(results)}")