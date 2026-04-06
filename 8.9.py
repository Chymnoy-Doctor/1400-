salaries = []
for worker in range(1, 13):
    print(f"\nРаботник {worker}")
    worker_salaries = []
    for month in range(1, 4):
        salary = float(input(f"  Зарплата за месяц {month}: "))
        worker_salaries.append(salary)
    salaries.append(worker_salaries)

# а) общая сумма за квартал всем работникам
total_all = 0
for worker in salaries:
    total_all += sum(worker)
print(f"\nа) Общая сумма за квартал: {total_all:.2f}")