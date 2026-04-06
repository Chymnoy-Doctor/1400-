n = int(input("Введите количество чисел: "))
sum_odd = 0
i = 0

while i < n:
    num = float(input("Введите число: "))
    if num == int(num) and int(num) % 2 != 0:
        sum_odd += num
        i += 1
    else:
        break

print(f"Сумма начальных нечётных чисел: {sum_odd}")