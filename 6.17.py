num1, den1 = 1, 1  # 1/1
num2, den2 = 2, 1  # 2/1
while True:
    num_next = num1 + num2
    den_next = den1 + den2
    val1 = num2 / den2
    val2 = num_next / den_next
    if abs(val2 - val1) <= 0.001:
        print(f"Первый член: {num2}/{den2} = {val2:.6f}")
        print(f"Следующий член: {num_next}/{den_next} = {val2:.6f}")
        print(f"Разница: {abs(val2 - val1):.6f}")
        break
    num1, den1 = num2, den2
    num2, den2 = num_next, den_next