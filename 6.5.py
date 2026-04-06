product = 1
while True:
    num = int(input("Введите положительное число (0 для окончания): "))
    if num == 0:
        print(0)
        break
    product *= num
    print(product)