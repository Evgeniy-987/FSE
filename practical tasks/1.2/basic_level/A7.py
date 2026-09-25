x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

color1 = (x1 + y1) % 2   # 0 — белая, 1 — чёрная
color2 = (x2 + y2) % 2

if color1 == color2:
    print("YES")
    print("White" if color1 == 0 else "Black")
else:
    print("NO")