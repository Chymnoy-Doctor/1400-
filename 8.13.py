scores = []
for athlete in range(1, 9):
    print(f"\nСпортсмен {athlete}")
    athlete_scores = []
    for sport in range(1, 6):
        score = float(input(f"  Баллы за вид спорта {sport}: "))
        athlete_scores.append(score)
    scores.append(athlete_scores)

max_score = max(max(athlete) for athlete in scores)
print(f"\nа) Максимальная оценка в таблице: {max_score:.2f}")