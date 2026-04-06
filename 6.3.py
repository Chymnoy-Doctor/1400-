numbers = []
for _ in range(18):
    numbers.append(int(input("Введите число: ")))
first = numbers[0]
count = 0
i = 0
while i < 18 and numbers[i] == first:
    count += 1
    i += 1
print(f"Количество начальных одинаковых элементов: {count}")