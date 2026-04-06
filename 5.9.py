import math
R = 6350 
print("Высота (км)\tРасстояние до горизонта (км)")
for h in range(1, 11):
    distance = math.sqrt(h * (2 * R + h))
    print(f"{h}\t\t{distance:.2f}")