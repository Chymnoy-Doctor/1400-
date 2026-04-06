print("Вариант 2: ввод/вывод по столбцам")
scores_table = []
for student in range(1, 19):
    scores_table.append([0, 0, 0])

for subject in range(1, 4):
    print(f"\nПредмет {subject}")
    for student in range(1, 19):
        score = int(input(f"  Оценка ученика {student}: "))
        scores_table[student-1][subject-1] = score

print("\nРезультаты:")
for student in range(18):
    print(f"Ученик {student+1}: {scores_table[student][0]} {scores_table[student][1]} {scores_table[student][2]}")