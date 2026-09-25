values = ["123e", "91.4", 524.345 ** 3, "7.1 + 4", "4 - 2", "42", -12.12]

for v in values:
    try:
        result = int(v)
        print(v, "-> можно, результат:", result)
    except:
        print(v, "-> нельзя")
        