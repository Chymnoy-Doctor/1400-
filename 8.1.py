print("а)")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
print("\nб)")
for i in range(5, 10):
    for j in range(i - 4):
        print(i, end=" ")
    print()