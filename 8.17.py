students = []
for grade in range(1, 12):
    print(f"\nПараллель {grade}")
    grade_students = []
    for letter in ['А', 'Б', 'В', 'Г']:
        count = int(input(f"  Класс {letter}: "))
        grade_students.append(count)
    students.append(grade_students)

print("\nа) Самая малочисленная параллель:")
min_parallel = min(sum(grade) for grade in students)
min_parallel_num = [i + 1 for i, grade in enumerate(students) if sum(grade) == min_parallel]
print(f"  Параллель(и) {min_parallel_num} с {min_parallel} учениками")
