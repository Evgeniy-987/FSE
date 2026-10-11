def get_quadrant(x: float, y: float) -> int:
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4

x1, y1, x2, y2 = map(float, input("Введите координаты x1, y1, x2, y2 (через пробел): ").split())

q1 = get_quadrant(x1, y1)
q2 = get_quadrant(x2, y2)

if q1 == q2:
    print(f"Точки лежат в одной четверти: {q1}")
else:
    print("Точки лежат в разных четвертях")