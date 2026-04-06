scores = []
for athlete in range(1, 16):
    print(f"\nСпортсмен {athlete}")
    athlete_scores = []
    for prog in range(1, 4):
        score = float(input(f"  Баллы за программу {prog}: "))
        athlete_scores.append(score)
    scores.append(athlete_scores)

print("\nа) Средний балл каждого спортсмена:")
for i, athlete in enumerate(scores, 1):
    avg = sum(athlete) / 3
    print(f"  Спортсмен {i}: {avg:.2f}")