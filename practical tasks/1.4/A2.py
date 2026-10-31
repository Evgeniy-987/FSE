# Ввод размеров с клавиатуры
n = int(input("Введите n (количество строк): "))
m = int(input("Введите m (количество столбцов): "))

# 1. Прямоугольник n * m
print(f"\nПРЯМОУГОЛЬНИК {n}*{m}:")
for i in range(n):
    for j in range(m):
        print("#", end="")
    print()

# 2. Рамка n * m
print(f"\nРАМКА {n}*{m}:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

# 3. Правый треугольник из n строк
print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(1, n + 1):
    for j in range(i):
        print("#", end="")
    print()