number = int(input("Введите 5-значное число: "))
sum_digits = (number // 10000) + (number // 1000 % 10) + (number // 100 % 10) + (number // 10 % 10) + (number % 10)
print(f"Сумма цифр: {sum_digits}")
