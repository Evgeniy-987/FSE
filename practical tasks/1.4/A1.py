import random
import time

n = int(input("Введите количество примеров: "))

correct_answers = 0
total_time = 0

for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    print(f"Вопрос {i}/{n}")

    start_time = time.time()
    answer = int(input(f"{a} x {b} = "))
    elapsed_time = round(time.time() - start_time, 1)

    total_time += elapsed_time

    if answer == a * b:
        correct_answers += 1
        print(f"Верно! (Время: {elapsed_time} сек)")
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {elapsed_time} сек)")

# Подсчёт и вывод статистики
avg_time = round(total_time / n, 1)
percent = round((correct_answers / n) * 100, 1)

print("\nСТАТИСТИКА:")
print(f"Общее время: {round(total_time, 1)} секунд")
print(f"Среднее время на вопрос: {avg_time} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных: {percent}%")