number = int(input("Введите 4-значное число: "))
sum_digits = (number // 1000) + (number // 100 % 10) + (number // 10 % 10) + (number % 10)
print(f"Сумма цифр: {sum_digits}")
