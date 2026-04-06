salaries = []
for worker in range(1, 13):
    print(f"\nРаботник {worker}")
    worker_salaries = []
    for month in range(1, 4):
        salary = float(input(f"  Зарплата за месяц {month}: "))
        worker_salaries.append(salary)
    salaries.append(worker_salaries)

print("\nб) Работник с наибольшей зарплатой в каждом месяце:")
for month in range(3):
    month_salaries = [salaries[worker][month] for worker in range(12)]
    max_worker = month_salaries.index(max(month_salaries)) + 1
    print(f"  Месяц {month + 1}: работник {max_worker}")