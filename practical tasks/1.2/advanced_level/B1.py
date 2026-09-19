from decimal import Decimal, ROUND_HALF_UP
from math import isclose
from pathlib import Path
import re

number = input("Введите номер входного файла: ")
folder = Path(__file__).parent
filename = folder / f"inmap{number}.dat"
output_filename = folder / f"outmap{number}.dat"

with open(filename, "r") as file:
    data = file.read().split()

locations = int(data[0])
scale = float(data[1])
distances_on_map = [float(value) for value in data[2:]]

distances_in_miles = [
    float(
        (Decimal(str(distance)) * Decimal(str(scale))).quantize(
            Decimal("0.1"), rounding=ROUND_HALF_UP
        )
    )
    for distance in distances_on_map
]
total_distance = sum(distances_in_miles)

print("Комар Е.В.")
print("Simple Map Distance Computations\n")
print(f"Map Scale Factor:    {scale:.2f} miles per inch\n")
print("      Map        Mileage")
print("      Measure    Distance")
print("=========================================================")

for index, (map_dist, mile_dist) in enumerate(
    zip(distances_on_map, distances_in_miles), start=1
):
    print(f"# {index:>2}   {map_dist:>5.1f}      {mile_dist:>5.1f}")

print("=========================================================")
print(f"Total Distance:     {total_distance:.1f} miles\n")

with open(output_filename, "r") as file:
    output_text = file.read()

expected_distances = [
    float(match.group(1))
    for match in re.finditer(r"^#\s+\d+\s+\S+\s+([\d.]+)$", output_text, re.MULTILINE)
]
total_match = re.search(r"Total Distance:\s+([\d.]+)\s+miles", output_text)

if total_match is None:
    raise ValueError("В выходном файле не найдено общее расстояние.")

expected_values = [float(total_match.group(1))] + expected_distances
calculated_values = [total_distance] + distances_in_miles

if len(expected_values) == len(calculated_values) and all(
    isclose(expected, actual, rel_tol=1e-9, abs_tol=1e-9)
    for expected, actual in zip(expected_values, calculated_values)
):
    print("Результаты совпадают с данными из выходного файла.")
else:
    print("Результаты не совпадают с данными из выходного файла.")