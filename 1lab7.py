import math
a = float(input("Введіть початкове значення a: "))
b = float(input("Введіть кінцеве значення b: "))
h = float(input("Введіть крок h: "))
x = a
while x <= b:
    try:
        if x == 0:
            raise ValueError("Ділення на 0!")
        f_x = math.exp(x) + math.sqrt(x) - 2 / x
        print(f"f({x}) = {f_x}")
    except ValueError as e:
        print(f"Помилка при обчисленні для x = {x}: {e}")
    x += h
