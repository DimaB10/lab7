import random
a = int(input("Введіть нижню межу a: "))
b = int(input("Введіть верхню межу b: "))
random_list = [random.randint(a, b) for _ in range(10)]
print("Згенерований список:", random_list)
max_element = max(random_list)
min_element = min(random_list)
print(f"Найбільший елемент: {max_element}")
print(f"Найменший елемент: {min_element}")