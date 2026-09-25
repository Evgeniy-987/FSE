import sys

number = 3 ** 9090001
size_bytes = sys.getsizeof(number)
size_mb = size_bytes / 1024 / 1024

print(f"Размер: {size_bytes} байт")
print(f"Это {size_mb:.4f} МБ")