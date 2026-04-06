count = 0
for num in range(100, 501):
    s = sum(int(d) for d in str(num))
    if s == 15:
        count += 1
print(f"Количество чисел от 100 до 500 с суммой цифр 15: {count}")